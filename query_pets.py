import sqlite3

def fetch_person(cur, person_id):
    cur.execute(
        "SELECT first_name, last_name, age FROM person WHERE id = ?",
        (person_id,),
    )
    return cur.fetchone()

def fetch_pets_for_person(cur, person_id):
    cur.execute(
        """
        SELECT p.name, p.breed, p.age, p.dead
        FROM pet AS p
        JOIN person_pet AS pp ON pp.pet_id = p.id
        WHERE pp.person_id = ?
        ORDER BY p.name
        """,
        (person_id,),
    )
    return cur.fetchall()

def main():
    con = sqlite3.connect("pets.db")
    cur = con.cursor()

    while True:
        raw = input("Please enter a person ID (-1 to exit): ").strip()
        if raw == "-1":
            break
        try:
            person_id = int(raw)
        except ValueError:
            print("Invalid input. Please enter a numeric ID or -1 to exit.")
            continue

        person = fetch_person(cur, person_id)
        if not person:
            print(f"Person with ID {person_id} does not exist.")
            continue

        first, last, age = person
        print(f"{first} {last}, {age} years old")

        pets = fetch_pets_for_person(cur, person_id)
        if not pets:
            print(f"{first} {last} does not own any pets.")
            continue

        for name, breed, pet_age, dead in pets:
            verb = "was" if dead else "is"
            print(f"{first} {last} owned {name}, a {breed}, that {verb} {pet_age} years old.")

    con.close()

if __name__ == "__main__":
    main()
