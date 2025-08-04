# Mini Project 22: Gradebook CSV Analyzer

## 📌 Objective
This Python script reads student names and marks from a CSV file, calculates grades based on the marks, and writes the final result (with grades) to a new CSV file.

## 🧠 Features
- Uses `csv.DictReader` to read structured input.
- Applies grading logic:
  - A: 90–100
  - B: 80–89
  - C: 70–79
  - D: 60–69
  - F: Below 60
- Outputs a formatted CSV file with Name, Marks, and Grade using `csv.DictWriter`.

## 📂 Files
- **Input:** `gradebook.csv`
- **Output:** `report_card.csv`

## 🛠 How to Run
1. Place `gradebook.csv` in the same directory.
2. Run the script using:
   ```
   python gradebook_analyzer.py
   ```
3. The output will be written to `report_card.csv`.

## 👨‍💻 Author
Dhruva
