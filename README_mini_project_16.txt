# Mini Project 16: Personal Habit Tracker 🧘‍♂️📈

A simple command-line tool to track daily habits and maintain streaks.

## ✅ Features

- Add new habits
- Mark habits as done for the day
- Automatically resets daily status
- View all habits with streaks and progress emojis
- Modular design with clean CLI

## 📁 Files

- `habit_tracker.py`: Main program with all logic and CLI menu.

## 💡 How It Works

- Each habit is stored as a dictionary with:
  - `name`: Habit name
  - `streak`: Number of consecutive days completed
  - `done_today`: Whether marked as done today

- At the start of each action, the program checks if a new day has started and resets accordingly.

## 🧪 Sample Output

```
--- Personal Habit Tracker ---
1. Add New Habit
2. Mark Habit as Done Today
3. View All Habits and Streaks
4. Exit

📊 Habit Tracker – Your Progress
╔════════════════════════════════════════╗
║ No │ Habit Name      │ Status & Streak ║
╠════╪════════════════╪═════════════════╣
║ 1  │ Reading         │ ✅ Done Today (🔥 3d) ║
║ 2  │ Meditation      │ ⏳ Pending (🔥 1d)     ║
╚════╧════════════════╧═════════════════╝
```

## 👨‍💻 Author

Dhruva, as part of the Data Science + AI Roadmap (Mini Project 16)
