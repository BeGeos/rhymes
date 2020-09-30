import random
import re

prompt = input('Do you prefer italian or english? ')
if prompt == 'italian':
    with open('italian.txt') as words:
        fh = words.read()
        text = fh.split('\n')
elif prompt == 'english':
    with open('english_words.txt') as words:
        fh = words.read()
        text = fh.split('\n')
else:
    print("No vocabulary named '{}'".format(prompt))

words.close()

rhyme = input('Please indicate a rhyme ')
n = input('And how many words would you like to know? ')
word = []
count = 0
for line in text:
    count += 1
    if line.endswith(rhyme):
        word.append(line)
print('There are {} words in the file'.format(count))
print("and only {} ends with '{}'".format(len(word), rhyme))
try:
    result = random.sample(word, int(n))
    print(result)
except ValueError as v:
    print(v)


