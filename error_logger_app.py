# Error Logger App
import datetime
import os

def log_error(error_message):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("error_log.txt", "a") as file:
        file.write(f"[{current_time}] ERROR: {error_message}\n")

def simulate_error():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        log_error("Division by zero error.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        log_error("Value error occurred.")
    except Exception as e:
        print("An unexpected error occurred.")
        log_error(str(e))

def view_log():
    if os.path.exists("error_log.txt"):
        with open("error_log.txt", "r") as file:
            print("=== Error Log ===")
            print(file.read())
    else:
        print("No error log found.")

def main():
    while True:
        print("\n=== Error Logger App ===")
        print("1. Simulate Error")
        print("2. View Log")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            simulate_error()
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("Exiting Error Logger App.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
