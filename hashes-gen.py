import hashlib
import sys

print(f'HASHES GENERATOR')
print('-' * 16)

while True:
    menu = int(input(''' ### MENU - Choose the hash type ###
                     1) MD5
                     2) SHA1
                     3) SHA256
                     4) SHA512
                     5) Exit
                     Choose the hash to be applied: '''))

    if menu == 5:
        print(f'Exiting...')
        sys.exit()
    elif 1 <= menu <= 4:
        string = input(f'\nType the text to be generated: ')

        if menu == 1:
            result = hashlib.md5(string.encode('utf-8'))
            print(f'\nMD5 hash of {string}: {result.hexdigest()}\n')
        elif menu == 2:
            result = hashlib.sha1(string.encode('utf-8'))
            print(f'\nSHA1 hash of {string}: {result.hexdigest()}\n')
        elif menu == 3:
            result = hashlib.sha256(string.encode('utf-8'))
            print(f'\nSHA256 hash of {string}: {result.hexdigest()}\n')
        elif menu == 4:
            result = hashlib.sha512(string.encode('utf-8'))
            print(f'\nSHA512 hash of {string}: {result.hexdigest()}\n')
    else:
        print(f'Option invalid, try again\n')
