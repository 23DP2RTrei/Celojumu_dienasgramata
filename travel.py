import os
import json
from rich.console import Console
from rich.table import Table

console = Console()
DATA_FILE = "trips.json"

# Funkcija, lai ielādētu datus
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        trips = json.load(file)

    # Automātiski pievieno aprakstu, ja nav
    for trip in trips:
        if "description" not in trip:
            trip["description"] = "Nav apraksta"
    return trips

# Funkcija, lai saglabātu datus
def save_data(trips):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(trips, file, indent=4, ensure_ascii=False)

# Funkcija izvēlnes attēlošanai
def show_menu():
    table = Table(title="📌 CEĻOJUMU PĀRVALDĪBA 📌", style="blue")
    table.add_column("Nr.", justify="center", style="cyan")
    table.add_column("Darbība", justify="left", style="green")

    menu_options = [
        ("1", "Pievienot jaunu ceļojumu"),
        ("2", "Skatīt visus ceļojumus"),
        ("3", "Meklēt ceļojumu pēc galamērķa"),
        ("4", "Rediģēt ceļojumu"),
        ("5", "Dzēst ceļojumu"),
        ("6", "Iziet"),
    ]

    for option in menu_options:
        table.add_row(option[0], option[1])

    console.print(table)

# Funkcija ceļojumu attēlošanai
def show_trips(trips):
    if not trips:
        console.print("[bold red]❌ Nav saglabātu ceļojumu![/bold red]")
        return

    table = Table(title="📍 Saglabātie ceļojumi 📍", style="yellow")
    table.add_column("Nr.", justify="center", style="red")
    table.add_column("Nosaukums", justify="left", style="green")
    table.add_column("Galamērķis", justify="left", style="cyan")
    table.add_column("Datums", justify="left", style="magenta")
    table.add_column("Apraksts", justify="left", style="white")

    for i, trip in enumerate(trips, 1):
        table.add_row(str(i), trip["name"], trip["destination"], trip["date"], trip["description"])

    console.print(table)

# Funkcija jauna ceļojuma pievienošanai
def add_trip(trips):
    name = input("Ievadi ceļojuma nosaukumu: ")
    destination = input("Ievadi galamērķi: ")
    date = input("Ievadi datumu (YYYY-MM-DD): ")
    description = input("Ievadi aprakstu par ceļojumu: ")

    trips.append({"name": name, "destination": destination, "date": date, "description": description})
    save_data(trips)
    console.print(f"[bold green]✅ Ceļojums '{name}' pievienots![/bold green]")

# Funkcija ceļojuma meklēšanai
def search_trip(trips):
    keyword = input("Ievadi meklējamo vārdu (galamērķī): ").lower()
    results = [trip for trip in trips if keyword in trip["destination"].lower() or keyword in trip["description"].lower()]

    if results:
        show_trips(results)
    else:
        console.print("[bold red]❌ Netika atrasts neviens ceļojums pēc meklēšanas kritērija![/bold red]")

# Funkcija ceļojuma rediģēšanai
def edit_trip(trips):
    show_trips(trips)
    try:
        idx = int(input("Ievadi rediģējamā ceļojuma numuru: ")) - 1
        if idx < 0 or idx >= len(trips):
            console.print("[bold red]❌ Nepareizs numurs![/bold red]")
            return

        trips[idx]["name"] = input("Jauns ceļojuma nosaukums: ")
        trips[idx]["destination"] = input("Jauns galamērķis: ")
        trips[idx]["date"] = input("Jauns datums (YYYY-MM-DD): ")
        trips[idx]["description"] = input("Jauns apraksts: ")

        save_data(trips)
        console.print("[bold green]✅ Ceļojums veiksmīgi rediģēts![/bold green]")
    except ValueError:
        console.print("[bold red]❌ Nepareiza ievade![/bold red]")

# Funkcija ceļojuma dzēšanai
def delete_trip(trips):
    show_trips(trips)
    try:
        idx = int(input("Ievadi dzēšamā ceļojuma numuru: ")) - 1
        if idx < 0 or idx >= len(trips):
            console.print("[bold red]❌ Nepareizs numurs![/bold red]")
            return

        deleted = trips.pop(idx)
        save_data(trips)
        console.print(f"[bold green]✅ Ceļojums '{deleted['name']}' dzēsts![/bold green]")
    except ValueError:
        console.print("[bold red]❌ Nepareiza ievade![/bold red]")

# Galvenā programma
def main():
    trips = load_data()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_menu()
        choice = input("👉 Izvēlieties opciju: ")

        if choice == "1":
            add_trip(trips)
        elif choice == "2":
            show_trips(trips)
        elif choice == "3":
            search_trip(trips)
        elif choice == "4":
            edit_trip(trips)
        elif choice == "5":
            delete_trip(trips)
        elif choice == "6":
            console.print("[bold red]👋 Programma izieta![/bold red]")
            break
        else:
            console.print("[bold red]❌ Nepareiza izvēle, mēģiniet vēlreiz![/bold red]")

        input("\nNospiediet Enter, lai turpinātu...")

if __name__ == "__main__":
    main()
