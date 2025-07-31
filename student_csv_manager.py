import csv

def add_student():
    name = input('Enter student name:')
    subject = input('Enter subject name:')
    marks = input('Enter subject marks:')
    with open('student.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, marks])
    print('Student record added successfully!')

def view_students():
    with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    name = input('Enter student name to search:').lower()
    with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name:
                print(f'Name: {row[0]}\nSubject: {row[1]}\nMarks: {row[2]}')
                return
        print('Student not found!')

def more_marks():
    limit = int(input('Enter the marks to choose the students:'))
    with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if int(row[2]) > limit:
                print(row)
                return
        else:
            print('No students found with more marks than the chosen marks!')

def main():
    while True:
        print('===Student Marks CSV Manager===')
        print('1. Add New Student Marks')
        print('2. View All Students')
        print('3. Search a Student by Name')
        print('4. More marks than Chosen Marks')
        print('5. Exit')
        op = int(input('Enter your choice:'))
        match op:
            case 1:
                add_student()
            case 2:
                view_students()
            case 3:
                search_student()
            case 4:
                more_marks()
            case 5:
                print('Thank you for using the application!')
                exit()
            case _:
                print('Invalid choice! Please try again')

main()
