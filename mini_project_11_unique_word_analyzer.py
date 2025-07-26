# Mini Project 11: Unique Word Analyzer

para = input('Enter a paragraph: ')
words = para.split()
unique_words = set(words)

print(f'Total Words: {len(words)}')
print(f'Unique Words: {len(unique_words)}')

sorted_unique = sorted(unique_words)
print('Sorted Unique Words:')
print(sorted_unique)
