
# Mini Project 14: Student Attendance Tracker 🎓

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    total_days = int(input("Enter total working days: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "days_present": 0,
        "total_days": total_days
    }
    students.append(student)
    print("\n✅ Student added!\n")

def mark_attendance():
    roll_no = input("Enter roll number to mark attendance: ")
    for student in students:
        if student["roll_no"] == roll_no:
            days = int(input("Days present to add: "))
            student["days_present"] += days
            print("\n✅ Attendance updated!\n")
            return
    print("\n❌ Student not found!\n")

def calculate_percentage(present, total):
    if total == 0:
        return 0.0
    return round((present / total) * 100, 2)

def get_status(percentage):
    return "Pass" if percentage >= 75 else "Low Attendance"

def view_report():
    if not students:
        print("\n📭 No student records to display!\n")
        return

    print("\n📊 Attendance Report:\n")
    print("-" * 70)
    print(f"| {'Roll No':<8} | {'Name':<12} | {'Present':<8} | {'Total':<6} | {'%':<6} | {'Status':<15} |")
    print("-" * 70)
    for s in students:
        percent = calculate_percentage(s["days_present"], s["total_days"])
        status = get_status(percent)
        print(f"| {s['roll_no']:<8} | {s['name']:<12} | {s['days_present']:<8} | {s['total_days']:<6} | {percent:<6} | {status:<15} |")
    print("-" * 70 + "\n")

def search_by_roll():
    roll_no = input("Enter roll number to search: ")
    found = False
    for s in students:
        if s["roll_no"] == roll_no:
            percent = calculate_percentage(s["days_present"], s["total_days"])
            status = get_status(percent)
            print("\n🎓 Student Found:")
            print("---------------------------")
            print(f"Name         : {s['name']}")
            print(f"Roll Number  : {s['roll_no']}")
            print(f"Days Present : {s['days_present']}")
            print(f"Total Days   : {s['total_days']}")
            print(f"Attendance % : {percent}%")
            print(f"Status       : {status}")
            print("---------------------------\n")
            found = True
            break
    if not found:
        print(f"\n❌ No student found with roll number {roll_no}!\n")

def main():
    while True:
        print("🎓 Student Attendance Tracker 🎓\n")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Search by Roll Number")
        print("5. Exit\n")

        choice = input("Choose an option: ")
        print()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_report()
        elif choice == "4":
            search_by_roll()
        elif choice == "5":
            print("👋 Exiting Attendance Tracker. Goodbye, Dhruva!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
