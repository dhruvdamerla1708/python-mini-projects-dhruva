# Mini Project 15: Text Analyzer Pro
text=input('Enter text:').lower()
a,count=text.split(),0
# to calculate the total number of characters in the text
for i in a:
  count+=len(i)
print(f'Total number of characters (no spaces): {count}')
# to calculate the total number of words in the text
print(f'Total number of words: {len(a)}')
# to calculate the total number of sentences in the text
print(f'Total number of sentences: {text.count(".")}')
# to calculate the frequency of each word in the text
freq={}
for i in a:
  freq[i]=freq.get(i,0)+1
print('Word Frequencies:')
for key,value in freq.items():
  print(f'{key} -> {value}')
# to calculate the unique words in the text
a.sort()
print(f'Unique Words (sorted): {sorted(set(a))}')
# longest word in the text
for i in a:
  if len(i)==max(len(i) for i in a):
    print(f'Longest word: {i}')
    break
# shortest word in the text
for i in a:
  if len(i)==min(len(i) for i in a):
    print(f'Shortest word: {i}')
    break
