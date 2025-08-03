import string

text = input('Enter a paragraph: ').lower()
freq = {}

print('Word Frequency Report:')
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

for word in cleaned_text.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f'{word}:{count}')
