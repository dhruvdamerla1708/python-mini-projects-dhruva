# Mini Project 9: Movie Record Keeper

movies = []

def add_movie():
    name = input('Enter the name of the movie: ')
    year = int(input('Enter the release year of the movie: '))
    rate = float(input('Enter the rating of the film: '))
    films = (name, year, rate)
    movies.append(films)

def display():
    if not movies:
        print('No movie is found')
    else:
        print('\nThe Movies are:')
        for i in movies:
            print(f"{i[0]} (Year: {i[1]}, Rating: {i[2]})")

def top_rated():
    if not movies:
        print('No movie data is found')
    else:
        rates = []
        for i in range(len(movies)):
            top = movies[i][2]
            rates.append(top)
        top_rated = max(rates)
        for i in range(len(movies)):
            if top_rated == movies[i][2]:
                print(f"Top-rated movie is: '{movies[i][0]}' with a rating of {movies[i][2]}")

def main():
    while True:
        print('\n===== Movie Record Keeper =====')
        print('1. Add a movie')
        print('2. Display all movies')
        print('3. Top-Rated Movie')
        print('4. Exit')
        op = int(input('Enter your choice: '))
        match op:
            case 1:
                add_movie()
            case 2:
                display()
            case 3:
                top_rated()
            case 4:
                exit()
            case _:
                print('Invalid choice')

main()
