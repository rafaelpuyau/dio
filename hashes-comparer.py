import hashlib

file1 = 'file_one.txt'
file2 = 'file_two.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The {file1} is different from {file2}')
else:
    print(f'The files are the same')

print(f'O hash do {file1} é {hash1.hexdigest()}')
print(f'O hash do {file2} é {hash2.hexdigest()}')
