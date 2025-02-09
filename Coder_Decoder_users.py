import Users
from Coder import encrypt
from Decoder import decrypt

# Odczytanie i zdeszyfrowanie danych użytkowników
def read_file():

    users_list = []
    odczyt = open("Users.csv",'r')
    if odczyt.readable():
        print('ok')
    else:
        print('no')

    for user in odczyt:
        user = user.split(',')
        val1 = user[0]
        val2 = user[1]
        val3 = user[2]
        val1 = decrypt(val1)
        val2 = decrypt(val2)
        val3 = decrypt(val3)
        u = Users.User(val1,val2,val3)
        users_list.append(u)
        print(users_list[0].login,users_list[0].email)
    odczyt.close()
    return users_list

# Szyfrowanie danych poprzez AES i generowanie klucza
def crypt(log,pas,em):
    val1 = encrypt(log)
    val2 = encrypt(pas)
    val3 = encrypt(em)
    res = '{},{},{},0\n'.format(val1,val2,val3)
    return res
#read_file()