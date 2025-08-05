# Mini Project 23: Feedback Analyzer

## 📄 Project Description
This project reads raw feedback from a text file (`feedback.txt`), processes and cleans each line, and exports a structured summary to a CSV file (`feedback_summary.csv`). It counts the number of words in each feedback, determines if the feedback is short or long, and checks for positive sentiment based on keywords.

## ✅ Features
- Reads feedback line by line from `feedback.txt`
- Cleans punctuation and normalizes text
- Counts number of words
- Labels feedback as "Short" (≤5 words) or "Long" (>5 words)
- Detects positive sentiment based on keywords (`great`, `loved`)
- Outputs structured summary to `feedback_summary.csv`

## 📂 Output CSV Columns
- **Feedback**: Cleaned feedback line
- **WordCount**: Number of words
- **LengthStatus**: Short or Long
- **IsPositive**: Yes or No (based on keyword match)

## 📌 How to Run
1. Place your feedback lines into a file named `feedback.txt`
2. Run the Python script
3. View the results in `feedback_summary.csv`

## 🧠 Skills Used
- File handling
- String processing
- CSV operations
- Conditional logic
