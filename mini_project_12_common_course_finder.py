# Mini Project 12: Common Course Finder

a = input('Enter courses for student A (comma separated): ')
b = input('Enter courses for student B (comma separated): ')

courses_a = set(a.split(','))
courses_b = set(b.split(','))

print(f'Common Courses: {courses_a.intersection(courses_b)}')
print(f'Courses unique to student A: {courses_a.difference(courses_b)}')
print(f'Courses unique to student B: {courses_b.difference(courses_a)}')
print(f'Are their course lists completely different? {courses_a.isdisjoint(courses_b)}')
