import csv

def calculate_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

# Read from gradebook.csv and write to report_card.csv
with open('gradebook.csv', 'r') as infile, open('report_card.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Name', 'Marks', 'Grade']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        grade = calculate_grade(row['Marks'])
        writer.writerow({'Name': row['Name'], 'Marks': row['Marks'], 'Grade': grade})
