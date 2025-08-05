import csv
import string

# Define positive keywords
keywords = ['great', 'loved']

# Read from feedback.txt and write to feedback_summary.csv
with open('feedback.txt', 'r') as infile, open('feedback_summary.csv', 'w', newline='') as outfile:
    fieldnames = ['Feedback', 'WordCount', 'LengthStatus', 'IsPositive']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for line in infile:
        cleaned = line.strip().translate(str.maketrans('', '', string.punctuation)).lower()
        word_count = len(cleaned.split())
        status = 'Short' if word_count <= 5 else 'Long'
        is_positive = 'Yes' if any(keyword in cleaned for keyword in keywords) else 'No'

        writer.writerow({
            'Feedback': cleaned,
            'WordCount': word_count,
            'LengthStatus': status,
            'IsPositive': is_positive
        })
