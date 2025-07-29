# Mini Project 15: Text Analyzer Pro

## 📌 Objective:
Build a text analysis tool that takes a paragraph as input and returns detailed statistics about the text.

## 🔍 Features:
- Counts total characters (excluding spaces)
- Counts total words and sentences
- Displays frequency of each word
- Displays a sorted list of unique words
- Identifies the longest and shortest word

## 🛠️ How It Works:
1. Input a paragraph.
2. The script converts the text to lowercase.
3. It splits the text into words and performs all analysis:
   - Character count (without spaces)
   - Word count
   - Sentence count using `.`
   - Word frequency using a dictionary
   - Sorted unique words
   - Longest and shortest word

## 🧪 Example Input:
```
Enter text: The quick brown fox jumps over the lazy dog. The fox was fast.
```

## 🧾 Example Output:
```
Total number of characters (no spaces): 43
Total number of words: 11
Total number of sentences: 2
Word Frequencies:
the -> 3
quick -> 1
brown -> 1
fox -> 2
...
Unique Words (sorted): ['brown', 'dog', 'fast', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the', 'was']
Longest word: jumps
Shortest word: fox
```

## ✅ Status:
Project completed successfully and logged as Mini Project 15 in the Data Science + AI roadmap.
