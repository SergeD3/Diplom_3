import random
from password_generator import PasswordGenerator


def generate_email() -> str:
    return f'сергей_чичкань_14_{random.randint(100, 999)}@yandex.ru'


def get_random_password(length: int) -> str:
    pwo = PasswordGenerator()
    pwo.minlen = 6
    pwo.maxlen = 15
    pwo.minuchars = 2
    pwo.minlchars = 3
    pwo.minnumbers = 1
    pwo.minschars = 1

    return pwo.non_duplicate_password(length)