import Coder
dic = {0:"0",1:"1",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def remove_additional_str(x):
    length = len(x)
#    print(length)
#    print(x[1],x[length-2])
    for i in dic:
        if dic[i]==x[1]:
            b1=i
        if dic[i]==x[length-2]:
            b2=i

#    print(b1,b2)

    cryptogram = x[b1:length-b2]
#   print("crypto: "+cryptogram)
    return cryptogram

# split block of information about character
def separate_one(cryptogram):
    a=[]
    one=""
    j=0
    for i in range(len(cryptogram)):
        j+=1
        one +=cryptogram[i]
        if j==4:
            j=0
            a.append(one)
            one=""
    return a

# hex --> bin info block
def conv(x):
    for i in dic:
        if dic[i]==x:
            b1 = i
            b1 = bin(b1)
            str(b1)
            b1 = b1[2:]
            b1=b1.zfill(4)
    return b1

# hex --> bin
def convert_Hex_Bin(a):
    #print("a:"+str(a))
    binary=""
    b=[]
    for i in a:
        if i[0] == "X":
            b.append(i)
            continue
#       print(i)
        hexal=i[2:4]
        binary +=conv(hexal[0])
        binary +=conv(hexal[1])
        position1=int(i[0])
        position2=int(i[1])
        r1 = Coder.swap(binary,position1) #negate bit
        r2 = Coder.swap(r1,position2) #negate bit
#        print(binary)
        r2 = r2[::-1]
#        print("reverse " + r2)
        b.append(r2)
        binary=""
    return b

# bin --> dec
def convert_Bin_Dec(b):
    c=[]
    #print("b:"+str(b))
    for i in b:
        if i[0] == "X":
            c.append(int(i[1:]))
            continue
        pot = 7
        decv = 0
        for j in i:
            if j == "1":
                decv+=2**pot
            pot-=1
        c.append(decv)
    #print("c:"+str(c))
    return c

# dec --> ASCII
def convert_to_ASCII(c):
    answer=""
    for i in c:
        x=chr(i)
        answer+=x
    return answer

def decrypt(encrypted_text): # Main function to encrypt
    dcr = remove_additional_str(encrypted_text)
    sep = separate_one(dcr)
    conv_H_B = convert_Hex_Bin(sep)
    conv_B_D = convert_Bin_Dec(conv_H_B)
    conv_ascii = convert_to_ASCII(conv_B_D)
    return conv_ascii   # decrypted text