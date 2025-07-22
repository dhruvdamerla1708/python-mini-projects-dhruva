
def main():
    print('===== Marks Analyzer =====\n')
    n = int(input('Enter the number of subjects: '))
    names, marks = [], []

    for i in range(1, n + 1):
        name = input(f'\nEnter subject {i} name: ')
        names.append(name)
        mark = int(input(f'Enter marks in {name}: '))
        marks.append(mark)

    new_names, new_marks = tuple(names), tuple(marks)
    length = len(new_names)
    total = sum(new_marks)
    avg = total / length
    highest = max(new_marks)
    lowest = min(new_marks)

    print('\n--- Subject-wise Marks ---')
    for i in range(length):
        print(f'{i+1}. {new_names[i]}: {new_marks[i]}')

    print('\n--- Performance Summary ---')
    for i in range(length):
        if new_marks[i] == highest:
            print(f'Highest Scored Subject: {new_names[i]} ({highest})')
    for i in range(length):
        if new_marks[i] == lowest:
            print(f'Lowest Scored Subject: {new_names[i]} ({lowest})')
    print(f'Total Marks: {total}')
    print(f'Average Marks: {avg:.2f}')
    print('\n===== End of Report =====')

main()
