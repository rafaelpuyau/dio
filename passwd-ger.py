import random
import string

print(f'Hey there! I\'ll generate a random password for you')
print(f'You should enter the size for this password [Minimum size is 6]')

while True:
    pw_size = int(input('Size of desired password: '))
    if pw_size < 6:
        print(f'Remember, the minimum size is 6. Try again')
    else:
        chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.:;/?'
        rnd = random.SystemRandom()
        passwd = ''.join(rnd.choice(chars) for i in range(pw_size))
        print(f'New password generated: {passwd}')
        break

print(f'Keep your password in a safe and easily accessible place')
