import itertools

string = input('String to be swapped: ')
result = itertools.permutations(string, len(string))

with open('wordlist.txt', 'w') as file:
    for char in result:
        file.writelines(''.join(char))
        file.write('\n')

print(f'Word list has been created successfully')
