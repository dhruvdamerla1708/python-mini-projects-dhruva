import csv
import json
def view_all_students():
  print('The Students with Age and Grades are:')
  with open('students.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
      print(row)
def add_student():
  with open('students.csv','a',newline='') as file:
    writer=csv.writer(file)
    name=input('Enter the name of the student:')
    age=input('Enter the age of the student:')
    grade=input('Enter the grade of the student:')
    writer.writerow([name,age,grade])
    print('Student added successfully!')
def update_student_grade():
  with open('students.csv','r') as file:
    reader=csv.DictReader(file)
    rows=list(reader)
    name=input('Enter the name of the student:')
    grade=input('Enter the new grade of the student:')
    for row in rows:
      if row['name']==name:
        row['grade']=grade
        print('Student grade updated successfully!')
        break
    else:
      print('Student not found!')
  with open('students.csv','w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=['name','age','grade'])
    writer.writeheader()
    writer.writerows(rows)
def save():
  with open('students.csv','r') as file:
    reader=csv.DictReader(file)
    data=list(reader)
    with open('students.json','w') as file:
      json.dump(data,file,indent=2)
    print('Data saved successfully!')
    print('Thank you for using the Student Data Transformer!')
    exit()
def main():
  while True:
    print("===== Student Data Transformer=====\n1.View All Students\n2.Add a Student\n3.Update Student grade\n4.Save and Exit\n")
    op=int(input('Enter your choice:'))
    match op:
      case 1:
        view_all_students()
      case 2:
        add_student()
      case 3:
        update_student_grade()
      case 4:
        save()
      case _:
        print("Invalid choice!Try again")
main()
