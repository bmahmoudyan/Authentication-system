from random import randint
from string import ascii_letters, digits, punctuation

SecretKey = r""
chars = ascii_letters + digits + punctuation

for _i in range(50):
    choice = randint(0, len(chars)-1)
    SecretKey += chars[choice]



