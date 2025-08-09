# 📁 Log File Analyzer

The **Log File Analyzer** is a Python mini project designed to analyze plain text log files. It reads a log file, counts basic statistics like total lines, words, characters, and log levels (Error, Warning, Info), and identifies the most frequently used words.

---

## ✅ Features

- 🔢 Total number of lines, words, characters
- 🔁 Counts unique words
- 💥 Detects number of ERROR entries
- ⚠️  Detects number of WARNING entries
- ℹ️  Detects number of INFO entries
- 📊 Displays top 5 most frequent words
- 📄 Saves analysis to `summary_report.txt`

---

## 🚀 How It Works

1. Prompts user to enter a log filename.
2. Opens and reads the file line-by-line.
3. Cleans the text and splits it into words.
4. Uses word frequency dictionary to count occurrences.
5. Checks for presence of "error", "warning", or "info" in each line.
6. Displays the summary in a clean formatted output.
7. Writes the same summary to `summary_report.txt`.

---

## 📦 Example Output

```plaintext
📁 Log File Analyzer
----------------------------
Enter log filename: logs.txt

✅ Total Lines       : 243
🧾 Total Words       : 1,578
🔠 Total Characters  : 12,489
🔁 Total Unique Words: 367
💥 Error Entries     : 15
⚠️  Warning Entries   : 27
ℹ️  Info Entries      : 201

Top 5 Most Frequent Words:
1. error    → 15 times
2. warning  → 27 times
3. info     → 201 times
4. failed   → 8 times
5. success  → 5 times

✅ Summary saved to: summary_report.txt
