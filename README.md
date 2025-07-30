# 📝 Personal Daily Logger

A simple diary application in Python that allows users to log their daily thoughts with timestamps, view their past entries, and count total entries.

---

## 🔧 Features

- Add a new diary entry with the current timestamp
- View all past entries
- Count the total number of diary entries
- Stores entries in a local file called `diary.txt`

---

## 💡 How It Works

1. The user selects from a menu:
   - Add entry
   - View diary
   - Count entries
   - Exit
2. Entries are stored in `diary.txt` with a timestamp using `datetime.now()`.
3. Each diary entry is stored on a new line and timestamped for reference.

---

## 📁 File Structure

- `personal_daily_logger.py` - Main script to run the application.
- `diary.txt` - Auto-generated file to store diary entries.

---

## 🧠 Skills Used

- File handling (`with open`, `read`, `write`, `append`)
- Exception handling (`try-except`)
- `datetime` module for timestamps
- Menu-driven programming
- Basic string formatting

---

## 🏁 How to Run

```bash
python personal_daily_logger.py
```

---

## 👤 Created by

Dhruva – as part of the Day 18 milestone in the Data Science + AI Roadmap.
