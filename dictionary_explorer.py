dic = {}

def add_pair():
    key = input('Enter key: ')
    value = input('Enter value: ')
    dic[key.lower()] = value
    print('Entry added successfully!!!')

def search_key():
    if not dic:
        print('The Dictionary is Empty')
    else:
        search_key = input('Enter the key to be searched: ').lower()
        if search_key in dic:
            print(f'Value : {dic[search_key]}')
        else:
            print('No such key is found in the dictionary')

def delete_key():
    if not dic:
        print('The Dictionary is Empty')
    else:
        delete_key = input('Enter the key to be deleted: ').lower()
        if delete_key in dic:
            dic.pop(delete_key)
            print('Key Deleted Successfully')
        else:
            print('No such key is found in the Dictionary')

def display_all():
    if not dic:
        print('The Dictionary is empty')
    else:
        for key, value in dic.items():
            print(f'{key.title()} : {value}')

def main():
    while True:
        print('===== Welcome to the Dictionary Explorer App =====\n1. Add Key-Value\n2. Search Key\n3. Delete Key\n4. Display All\n5. Exit\n')
        try:
            op = int(input('Enter the choice: '))
            match op:
                case 1:
                    add_pair()
                case 2:
                    search_key()
                case 3:
                    delete_key()
                case 4:
                    display_all()
                case 5:
                    print('Exiting the program...')
                    break
                case _:
                    print('Invalid! Try again')
        except ValueError:
            print('Please enter a valid number.')
        print('\n---------------------------------------------\n')

main()
