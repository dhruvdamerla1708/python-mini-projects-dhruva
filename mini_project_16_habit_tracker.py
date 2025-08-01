# Mini Project 16: Personal Habit Tracker

from datetime import date

# List of habits (each habit is a dictionary)
habits = []

# Tracks last date the habits were updated to reset daily status
last_updated_date = None

def reset_habits_if_new_day():
    global last_updated_date
    today = date.today()

    if last_updated_date != today:
        for habit in habits:
            if habit["done_today"] == False:
                habit["streak"] = 0  # missed today, reset streak
            habit["done_today"] = False  # reset status for new day
        last_updated_date = today

def add_habit():
    reset_habits_if_new_day()
    name = input("Enter the habit you want to add: ")
    habits.append({"name": name, "streak": 0, "done_today": False})
    print(f"✅ Habit '{name}' added successfully!")

def mark_habit_done():
    reset_habits_if_new_day()
    if not habits:
        print("❗ No habits to mark. Please add some first.")
        return

    print("📋 Your Habits:")
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']}")

    try:
        choice = int(input("Select a habit number to mark as done: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            if not habit["done_today"]:
                habit["done_today"] = True
                habit["streak"] += 1
                print(f"✔️ Marked '{habit['name']}' as done for today.")
            else:
                print(f"🔁 You already marked '{habit['name']}' today.")
        else:
            print("❗ Invalid habit number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def view_habits():
    reset_habits_if_new_day()
    if not habits:
        print("📂 No habits to display.")
        return

    print("\n📊 Habit Tracker – Your Progress")
    print("╔════════════════════════════════════════╗")
    print("║ No │ Habit Name      │ Status & Streak ║")
    print("╠════╪════════════════╪═════════════════╣")
    for i, habit in enumerate(habits, start=1):
        status = "✅ Done Today" if habit["done_today"] else "⏳ Pending"
        print(f"║ {i:<2} │ {habit['name']:<14} │ {status} (🔥 {habit['streak']}d) ║")
    print("╚════╧════════════════╧═════════════════╝")

def main():
    while True:
        print("\n--- Personal Habit Tracker ---")
        print("1. Add New Habit")
        print("2. Mark Habit as Done Today")
        print("3. View All Habits and Streaks")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_habit()
                case 2:
                    mark_habit_done()
                case 3:
                    view_habits()
                case 4:
                    print("👋 Thank you for using the Personal Habit Tracker!")
                    break
                case _:
                    print("❗ Invalid choice. Please try again.")
        except ValueError:
            print("❗ Please enter a number.")

if __name__ == "__main__":
    main()
