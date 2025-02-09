import random
dic = {0:"0",1:"1",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

# two unique positions to negate in ASCII binary string
def random_int_positionst():
    r1 = random.randint(0,7)
    r2 = random.randint(0,7)

    while r1 == r2: # until get diffrent positions
        r2 = random.randint(0, 7)
    return [r1,r2] # positons

# add before and after cryptogram random hex characters
def add_redundancy(x):
    text=""
    front = random.randint(2,15)
    back = random.randint(2,15)
    # add front string
    for i in range(front):
        if i == 1: # add length of front string in second position
            text+=dic[front]
            continue
        r = random.randint(0,15)
        text+=dic[r] # add random characters

    text += str(x)
    # add back string
    for i in range(back):
        if i == (back-2): # add length of back string in penultimate position
            text+=dic[back]
            continue
        r = random.randint(0,15)
        text+=dic[r] # add random characters

    print("Length of strings, front/back: "+str(front)+"/"+str(back))
    return text

# create blocks of cryptogram
def bin_hex(bin_str,rand):
    bin_str=bin_str[::-1]
    pot=0
    value=0
    char = ""
    for i in bin_str:
        if i == "1":
            value+=2**pot
        pot+=1
    # create block of converted character
    hex_str = hex(value)
    hex_str = hex_str[2:].upper()
    hex_str = hex_str.zfill(2)

    # create block with positions
    char+=str(rand[0])
    char += str(rand[1])
    char+=hex_str
    return char

# negate bits in two random chosen positions
def swap(rev,val):
    iterator=0
    result = ""
    for i in rev:
        if iterator == val:
            if i == "0":
                result+="1"
            elif i == "1":
                result+="0"
        else:
            result+=i
        iterator+=1
    return result

def encrypt(text):  # Main function to encrypt
    cryptogram = ""
    for i in text:
        #print(i + " In ASCII DEC = " + str(ord(i)))
        dec = str(ord(i))   # conversion character to ASCII decimal
        if int(dec) > 255:
            cryptogram += "X{}".format(dec)
        else:
            b1 = bin(int(dec))  # conversion decimal to ASCII binary
            str(b1)
            b1 = b1[2:]
            b1 = b1.zfill(8)
            rev = b1[::-1]      # string reverse
            #print("Reverse: " + rev)

            val = random_int_positionst()  # random two positions
            #print("Positions: " + str(val))
            r1 = swap(rev, val[0])  #negate bit
            r2 = swap(r1,val[1])    #negate bit
            #print("Final: "+r2)
            bin_hex(r2,val)         #conversion bin --> hex
            cryptogram+=bin_hex(r2,val)
    #print("crypt: "+cryptogram)
    cryptogram = add_redundancy(cryptogram)    # add useless characters front/back
    return cryptogram # final cryptogram