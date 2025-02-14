import random
import string
from File_operations import read_users_file

def gen_with_length(x):
    y = ""
    for i in range(x):
        y += random.choice(string.ascii_letters + string.digits + "!@#$%")
    return y

def generate_verify_code():
    code = ''
    x = random.randint(5,10)
    print(x)
    for i in range(x):
        code+=random.choice(string.ascii_letters + string.digits + "!@#$%" )
    print(code)
    return code


def generate_unique_id():
    users_id = []
    id = ""
    id = gen_with_length(10)
    users = read_users_file()
    for user in users:
        users_id.append(user.id)
    print(users_id)
    while id in users_id:
        id = ""
        id = gen_with_length(10)
    print(id)
    return id
