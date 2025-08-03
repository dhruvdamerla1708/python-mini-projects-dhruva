# Mini Project 20: Word Frequency Analyzer

## Objective
Analyze the frequency of each word in a paragraph entered by the user.

## Features
- Accepts paragraph input from the user.
- Converts the input to lowercase.
- Removes punctuation for accurate word separation.
- Uses a dictionary to count the frequency of each word.
- Displays each word and its corresponding frequency.

## Sample Input
```
Enter a paragraph: Boomer helps Dhruva. Boomer is awesome!
```

## Sample Output
```
Word Frequency Report:
boomer: 2
helps: 1
dhruva: 1
is: 1
awesome: 1
```

## Concepts Used
- String manipulation
- Punctuation removal using `str.translate` and `string.punctuation`
- Dictionaries and `.get()` method
- Looping through `.split()` and `.items()`
