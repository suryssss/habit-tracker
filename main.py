from models.user import User
from services.habit_manager import HabitManager

def show_menu():
    print("\n--- Habit Tracker ---")
    print("1. Add Habit")
    print("2. Mark Habit Completed Today")
    print("3. View Habits")
    print("4. Exit")

def main():
    user = User("Suryzz")
    manager = HabitManager(user)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Habit name: ").strip()
            frequency = input("Frequency (daily/weekly): ").strip().lower()
            try:
                manager.create_habit(name, frequency)
                print("Habit added.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            habits = manager.get_habit_names()
            if not habits:
                print("No habits found.")
                continue

            print("Habits:", ", ".join(habits))
            name = input("Which habit did you complete today? ").strip()

            try:
                manager.complete_habit_today(name)
                print("Habit marked as completed.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            habits = manager.list_habits()
            if not habits:
                print("No habits to show.")
                continue

            for name, current, longest in habits:
                print(f"{name} | Current: {current} | Longest: {longest}")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
