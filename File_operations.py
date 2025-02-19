import Users
from Coder import encrypt
from Decoder import decrypt
from Record import Record


# Odczytanie i zdeszyfrowanie danych użytkowników
def read_users_file():
    users_list = []
    read = open("Users.csv",'r')
    if read.readable():
        print('Users.csv ok read')
    else:
        print('Users.csv no read')

    for user in read:
        user = user.split(',')
        val0 = user[0]
        val1 = user[1]
        val2 = user[2]
        val3 = user[3]

        val0 = decrypt(val0)
        val1 = decrypt(val1)
        val2 = decrypt(val2)
        val3 = decrypt(val3)
        u = Users.User(val0,val1,val2,val3)
        users_list.append(u)
    read.close()
    return users_list

def read_records(user):
    records = []
    read = open("Pass/{}.csv".format(user.id),'r')
    if read.readable():
        print('Pass/{}.csv ok read'.format(user.id))
    else:
        print('Pass/{}.csv no read'.format(user.id))
    for record in read:
        record = record.split(',')
        serv = decrypt(record[0])
        log = decrypt(record[1])
        pas = decrypt(record[2])
        r = Record(serv,log,pas)
        records.append(r)
    read.close()
    return records
# Szyfrowanie danych
def crypt(user_id,log,pas,em):
    user_id = str(user_id)
    val0 = encrypt(user_id)
    val1 = encrypt(log)
    val2 = encrypt(pas)
    val3 = encrypt(em)
    res = '{},{},{},{},0\n'.format(val0,val1,val2,val3)
    return res

def encrypt_record(serv,log,pas):
    val0 = encrypt(serv)
    val1 = encrypt(log)
    val2 = encrypt(pas)
    res = '{},{},{},0\n'.format(val0,val1,val2)
    return res