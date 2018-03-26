# coding=utf-8

def convert(c, key, start = 'a', n = 26):
    a = ord(start)
    offset = ((ord(c) - a + key)%n)
    return chr(a + offset)
def caesarEncode(s, key):
    o = ""
    for c in s:
        if c.islower():
            o+= convert(c, key, 'a')
        elif c.isupper():
            o+= convert(c, key, 'A')
        else:
            o+= c
    return o
def caesarDecode(s, key):
    return caesarEncode(s, -key)
if __name__ == '__main__':

    for key in range(26):
       e='daczcasdqwdcsdzasd'     #写这里
       d = caesarDecode(e, key)

       print d
       print '\n'