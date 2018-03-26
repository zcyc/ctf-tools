#coding=utf-8
def Decode(C,key,P):
    P = ''
    C=C.replace(' ','')
    C=C.upper()
    key=key.replace(' ','')
    key=key.upper()
    if len(C)!=len(key):
        i=len(C)/len(key)
        j=len(C)%len(key)
        tempKey=''
        for loop in range(0,i):
            tempKey=tempKey+key
        for loop in range(0,j):
            tempKey=tempKey+key[loop]
        key=tempKey

    CList = list(C)
    keyList = list(key)

    for i in range(0, len(C)):
        if (CList[i] >= 'A' and CList[i] <= 'Z'):
            temp = (26 + (ord(CList[i]) - ord(keyList[i]))) % 26 + ord('A')
            P = P + chr(temp)
        else:
            P = P + CList[i]
    print u'解密后：\n' + P

def Encode(C,key,P):
    C = ''
    P=P.replace(' ','')
    P=P.upper()
    key=key.replace(' ','')
    key = key.upper()
    if (len(P)!=len(key)):
        i = len(P) / len(key)
        j = len(P) % len(key)
        tempKey = ''
        for loop in range(0, i):
            tempKey = tempKey + key
        for loop in range(0, j):
            tempKey = tempKey + key[loop]
        key = tempKey

    PList = list(P)
    keyList = list(key)
    for i in range(0, len(P)):
        if (PList[i] >= 'A' and PList[i] <= 'Z'):
            temp = (ord(PList[i]) + ord(keyList[i])) % 26 + ord('A')
            C = C + chr(temp)
        else:
            C = C + PList[i]
    tempC = ''
    for i in range(0,len(C)):
        tempC = tempC + C[i]
        if (i+1)%5==0 and i!=len(C)-1:
            tempC=tempC+' '

    C=tempC
    print u'加密后:\n' + C

# 密文
C='r5yG lp9I BjM tFhB'

# 密钥
key='T6uh y7iJ QsZ bhMT'

# 明文
P='MEET ME AFTER SCHOOL'

# 解密
Decode(C,key,P)

# 加密
Encode(C,key,P)