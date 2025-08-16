import random
import string
import data
import copy

from faker import Faker
from password_generator import PasswordGenerator


fake = Faker('en_US')


def get_random_password(length: int) -> str:
    pwo = PasswordGenerator()
    pwo.minlen = 6
    pwo.maxlen = 15
    pwo.minuchars = 2
    pwo.minlchars = 3
    pwo.minnumbers = 1
    pwo.minschars = 1

    return pwo.non_duplicate_password(length)


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def get_random_user_credentials():
    creds_copy = copy.deepcopy(data.USER_BODY)

    login = generate_random_string(10)
    password = generate_random_string(10)
    email = fake.email(domain='yandex.ru')

    creds_copy['name'] = login
    creds_copy['password'] = password
    creds_copy['email'] = email

    return creds_copy


def get_random_email():
    email = fake.email(domain='yandex.ru')

    return email
