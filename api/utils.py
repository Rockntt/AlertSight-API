from string import ascii_letters, digits
from random import choice

def filename_generator(extension, alphabet=ascii_letters + digits, length=16):
    return (''.join(choice(alphabet) for i in range(length)) + '.' + extension)