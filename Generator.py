import random
import string
def generate():
    code = ''
    x = random.randint(5,10)
    print(x)
    for i in range(x):
        code+=random.choice(string.ascii_letters + string.digits + "!@#$%" )
    print(code)
    return code
