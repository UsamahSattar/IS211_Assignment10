import sqlite3

def main():
    con = sqlite3.connect("pets.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name  TEXT,
            age INTEGER
        );

        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name  TEXT,
            breed TEXT,
            age   INTEGER,
            dead  INTEGER
        );

        CREATE TABLE IF NOT EXISTS person_pet (
            person_id INTEGER,
            pet_id    INTEGER
        );
        """
    )

    
    cur.execute("DELETE FROM person_pet")
    cur.execute("DELETE FROM pet")
    cur.execute("DELETE FROM person")

    
    cur.executemany(
        "INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?);",
        [
            (1, "James",   "Smith",  41),
            (2, "Diana",   "Greene", 23),
            (3, "Sara",    "White",  27),
            (4, "William", "Gibson", 23),
        ],
    )

    cur.executemany(
        "INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?);",
        [
            (1, "Rusty", "Dalmation",         4, 1),
            (2, "Bella", "Alaskan Malamute",  3, 0),
            (3, "Max",   "Cocker Spaniel",    1, 0),
            (4, "Rocky", "Beagle",            7, 0),
            (5, "Rufus", "Cocker Spaniel",    1, 0),
            (6, "Spot",  "Bloodhound",        2, 1),
        ],
    )

    cur.executemany(
        "INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?);",
        [
            (1, 1),
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 5),
            (4, 6),
        ],
    )

    con.commit()
    con.close()

if __name__ == "__main__":
    main()
