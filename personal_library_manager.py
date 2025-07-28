# Personal Library Manager

books, count = {}, 1

def add_book():
    global count
    title = input("Enter the title of the book: ").lower()
    author = input("Enter the author of the book: ").lower()
    year = input("Enter the year of publication: ").lower()
    genre = input("Enter the genre of the book: ").lower()
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    books[count] = book
    count += 1

def display_books():
    print("Books in the library: ")
    print('Title\t\tAuthor\t\tYear\t\tGenre\n')
    for i, j in books.items():
        for k in j:
            print(j[k], end='\t\t')
        print()

def search_book():
    search = input("Enter the title or author of the book to search: ").lower()
    for i in books:
        if books[i]['title'] == search or books[i]['author'] == search:
            print(books[i])
            return
    print("Book not found")

def delete_book():
    title = input("Enter the title of the book to delete: ").lower()
    for i in list(books):
        if books[i]['title'] == title:
            del books[i]
            print("Book deleted successfully")
            return
    print("Book not found")

def main():
    while True:
        print('\n===== Personal Library Manager =====')
        print('1. Add a New Book')
        print('2. Display All Books')
        print('3. Search By Book')
        print('4. Delete Book By Title')
        print('5. Exit')
        op = int(input("Enter your choice: "))
        match op:
            case 1:
                add_book()
            case 2:
                display_books()
            case 3:
                search_book()
            case 4:
                delete_book()
            case 5:
                print('Exiting... Thank you for using Personal Library Manager')
                exit()
            case _:
                print("Invalid Choice")

main()
