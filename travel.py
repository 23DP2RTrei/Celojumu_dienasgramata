import json
from tabulate import tabulate

class TravelDiary:
    def __init__(self, filename="travel_data.json"):
        self.filename = filename
        self.trips = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.trips, file, indent=4, ensure_ascii=False)

    def add_trip(self, destination, start_date, end_date, description):
        trip = {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "description": description
        }
        self.trips.append(trip)
        self.save_data()
        print("Ceļojums pievienots!")

    def display_trips(self):
        if not self.trips:
            print("Nav pievienotu ceļojumu.")
            return
        print(tabulate(self.trips, headers="keys", tablefmt="grid"))

    def search_trips(self, keyword):
        results = [trip for trip in self.trips if keyword.lower() in trip["destination"].lower()]
        if results:
            print(tabulate(results, headers="keys", tablefmt="grid"))
        else:
            print("Nav atrastu ceļojumu pēc šī kritērija.")

    def delete_trip(self, destination):
        self.trips = [trip for trip in self.trips if trip["destination"].lower() != destination.lower()]
        self.save_data()
        print("Ceļojums dzēsts!")

    def count_trips(self):
        print(f"Kopējais ceļojumu skaits: {len(self.trips)}")


def main():
    diary = TravelDiary()
    while True:
        print("\n1. Pievienot ceļojumu")
        print("2. Parādīt visus ceļojumus")
        print("3. Meklēt ceļojumu")
        print("4. Dzēst ceļojumu")
        print("5. Kopējais ceļojumu skaits")
        print("6. Iziet")
        choice = input("Izvēlies darbību: ")
        
        if choice == "1":
            dest = input("Ievadi galamērķi: ")
            start = input("Ievadi sākuma datumu: ")
            end = input("Ievadi beigu datumu: ")
            desc = input("Apraksts: ")
            diary.add_trip(dest, start, end, desc)
        elif choice == "2":
            diary.display_trips()
        elif choice == "3":
            keyword = input("Ievadi meklējamo vārdu: ")
            diary.search_trips(keyword)
        elif choice == "4":
            dest = input("Ievadi dzēšamā ceļojuma galamērķi: ")
            diary.delete_trip(dest)
        elif choice == "5":
            diary.count_trips()
        elif choice == "6":
            print("Programma beidzas.")
            break
        else:
            print("Nepareiza izvēle, mēģini vēlreiz.")

if __name__ == "__main__":
    main()
