import json
import os

FILE_NAME = "trips.json"

def load_trips():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_trips(trips):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(trips, file, indent=4, ensure_ascii=False)

def add_trip():
    title = input("Ievadi ceļojuma nosaukumu: ")
    description = input("Ievadi aprakstu: ")
    date = input("Ievadi datumu (YYYY-MM-DD): ")
    country = input("Ievadi valsti: ")
    
    trip = {"title": title, "description": description, "date": date, "country": country}
    trips = load_trips()
    trips.append(trip)
    save_trips(trips)
    print("\nCeļojums saglabāts!\n")

def view_trips():
    trips = load_trips()
    if not trips:
        print("\nNav saglabātu ceļojumu.\n")
        return
    
    print("\nTavi ceļojumi:")
    for i, trip in enumerate(trips, start=1):
        print(f"{i}. {trip['title']} ({trip['date']}, {trip['country']}) - {trip['description']}")
    print()

def main():
    while True:
        print("1. Pievienot jaunu ceļojumu")
        print("2. Skatīt ceļojumus")
        print("3. Iziet")
        choice = input("Izvēlies opciju: ")
        
        if choice == "1":
            add_trip()
        elif choice == "2":
            view_trips()
        elif choice == "3":
            print("\nUz redzēšanos!")
            break
        else:
            print("\nNepareiza opcija, mēģini vēlreiz.\n")

if __name__ == "__main__":
    main()
