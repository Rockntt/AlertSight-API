from string import ascii_letters, digits
from random import choice


def filename_generator(extension, alphabet=ascii_letters + digits, length=16):
    """Генерация случайного имени для файла из букв латинскоаго алфавита и десятичных цифр"""
    return (''.join(choice(alphabet) for i in range(length)) + '.' + extension)
