# Personal Library Manager

This is a simple command-line application built using Python dictionaries to help manage a personal book collection. 

## Features

- **Add a New Book**: Input the title, author, publication year, and genre of the book.
- **Display All Books**: See all the books in a formatted table.
- **Search By Book**: Search for a book by its title or author.
- **Delete Book By Title**: Remove a book from the library using its title.
- **Exit**: Quit the application.

## Data Structure Used

- Books are stored in a dictionary with a numeric ID as the key.
- Each book is itself a dictionary with `title`, `author`, `year`, and `genre`.

## Sample Structure

```python
books = {
    1: {'title': 'book1', 'author': 'author1', 'year': '2021', 'genre': 'fiction'},
    2: {'title': 'book2', 'author': 'author2', 'year': '2022', 'genre': 'non-fiction'}
}
```

## How to Use

Run the program and use the menu options (1 to 5) to interact with your personal library.

Enjoy managing your books!
