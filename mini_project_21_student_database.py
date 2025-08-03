# Mini Project 21: Student Database System

students = {}

def add_student():
    roll_number = int(input("Enter student roll number: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    students[roll_number] = {"name": name, "age": age, "course": course}
    print("Student added successfully")

def search_student():
    roll_number = int(input("Enter student roll number: "))
    if roll_number in students:
        print("Student found:")
        print("Name:", students[roll_number]["name"])
        print("Age:", students[roll_number]["age"])
        print("Course:", students[roll_number]["course"])
    else:
        print("Student not found")

def update_student():
    roll_number = int(input("Enter student roll number: "))
    key = input("Enter the field to update: ").lower()
    value = input("Enter the new value: ")
    if roll_number in students:
        students[roll_number][key] = value
        print("Record updated successfully")
    else:
        print("Student not found")

def delete_student():
    roll_number = int(input("Enter student roll number: "))
    if roll_number in students:
        del students[roll_number]
        print("Student deleted successfully")
    else:
        print("Student not found")

def view_student():
    for roll_number, student in students.items():
        print(f'Roll Number: {roll_number:<10} | Name: {student["name"]:<10} | Age: {student["age"]:<10} | Course: {student["course"]:<10}')

def main():
    while True:
        print("\nWelcome to Student Database System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. View all Students")
        print("6. Exit")
        op = int(input("Enter your choice: "))
        match op:
            case 1:
                add_student()
            case 2:
                search_student()
            case 3:
                update_student()
            case 4:
                delete_student()
            case 5:
                view_student()
            case 6:
                print("Thank you for using Student Database System")
                break
            case _:
                print("Invalid choice! Try again")

if __name__ == "__main__":
    main()
