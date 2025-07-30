# personal_daily_logger.py
from datetime import datetime

def write_diary():
    line = input('Write your entry: ')
    with open('diary.txt', 'a') as d:
        d.write(f'\n{datetime.now()}:- {line}\n')
    print('Entry saved with timestamp!')

def view_diary():
    try:
        with open('diary.txt', 'r') as d:
            print(d.read())
    except FileNotFoundError:
        print('Diary is empty!')

def count_diary():
    with open('diary.txt', 'r') as d:
        print(f'Total entries: {len(d.readlines()) // 2}')

def main():
    while True:
        print('Welcome to Personal Daily Logger\n')
        print('1. Write a new diary entry')
        print('2. View all diary entries')
        print('3. Count total entries')
        print('4. Exit')
        op = int(input('Enter your choice: '))
        match op:
            case 1:
                write_diary()
            case 2:
                view_diary()
            case 3:
                count_diary()
            case 4:
                print('Goodbye, Dhruva!')
                exit()
            case _:
                print('Invalid choice! Try again.')

main()
