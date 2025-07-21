
# Mini Project 5: Student Report Card Generator

students = []
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    for j in range(num_subjects):
        mark = int(input(f"Enter marks for Subject {j+1}: "))
        marks.append(mark)
    students.append([name] + marks)

print("\n------ REPORT CARD ------")
for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / num_subjects

    if average >= 85:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'Fail'

    print(f"\nName: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
