vowels = ['a', 'e', 'i', 'o', 'u']

word = input('Provide a word to search for vowels: ')

found = {}

for letter in word:
    if letter in vowels:
        ''' Will produce Key Error - missing initialization '''
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

