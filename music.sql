
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS artists (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS albums (
    id          INTEGER PRIMARY KEY,
    artist_id   INTEGER NOT NULL,
    title       TEXT    NOT NULL,
    release_year INTEGER,
    
    UNIQUE (artist_id, title),
    FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS songs (
    id              INTEGER PRIMARY KEY,
    album_id        INTEGER NOT NULL,
    track_number    INTEGER NOT NULL,
    title           TEXT    NOT NULL,
    duration_seconds INTEGER NOT NULL CHECK (duration_seconds > 0),
    
    UNIQUE (album_id, track_number),
    UNIQUE (album_id, title),
    FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE INDEX IF NOT EXISTS idx_albums_artist ON albums(artist_id);
CREATE INDEX IF NOT EXISTS idx_songs_album  ON songs(album_id);

