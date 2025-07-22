def main():
    print('===== Travel History Tracker =====\n')
    n=int(input('Enter the number of places you visited: '))
    cities,years=[],[]
    for i in range(1,n+1):
        city=input(f'\nEnter city {i} name: ')
        cities.append(city)
        year=int(input('Enter year of visit: '))
        years.append(year)
    new_cities,new_years=tuple(cities),tuple(years)
    print('\n--- Your Travel History ---')
    for i in range(len(new_cities)):
        print(f'{i+1}. {new_cities[i]} ({new_years[i]})')
    year=int(input('\nEnter a year to search: '))
    if year in new_years:
        a=new_years.count(year)
        print(f'You visited {a} in {year}')
    else:
        print(f'No places were visted in the year {year}')
    print(f'\nFirst visited city: {new_cities[0]}')
    print(f'Most recent city in record: {new_cities[-1]}')
    print('\n===== End of Tracker =====')

main()
