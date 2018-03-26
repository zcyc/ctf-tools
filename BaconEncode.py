#coding:utf-8

def bec1(m):
    basic1 = {
        'A':'AAAAA',
        'B':'AAAAB',
        'C':'AAABA',
        'D':'AAABB',
        'E':'AABAA',
        'F':'AABAB',
        'G':'AABBA',
        'H':'AABBB',
        'I':'ABAAA',
        'J':'ABAAB',
        'K':'ABABA',
        'L':'ABABB',
        'N':'ABBAB',
        'O':'ABBBA',
        'P':'ABBBB',
        'Q':'BAAAA',
        'R':'BAAAB',
        'S':'BAABA',
        'T':'BAABB',
        'U':'BABAA',
        'V':'BABAB',
        'W':'BABBA',
        'X':'BABBB',
        'Y':'BBAAA',
        'Z':'BBAAB' 
    }
    output = ''
    for i in range(0, len(m), 1):
        temp = m[i: i + 1]
        output += basic1[temp]
    return output

def bec2(m):
    basic2 = {
        'A':'AAAAA',
        'B':'AAAAB',
        'C':'AAABA',
        'D':'AAABB',
        'E':'AABAA',
        'F':'AABAB',
        'G':'AABBA',
        'H':'AABBB',
        'I':'ABAAA',
        'J':'ABAAA',
        'K':'ABAAB',
        'L':'ABABA',
        'M':'ABABB',
        'N':'ABBAA',
        'O':'ABBAB',
        'P':'ABBBA',
        'Q':'ABBBB',
        'R':'BAAAA',
        'S':'BAAAB',
        'T':'BAABA',
        'U':'BAABB',
        'V':'BAABB',
        'W':'BABAA',
        'X':'BABAB',
        'Y':'BABBA',
        'Z':'BABBB',
        
    }
    output = ''
    for i in range(0, len(m), 1):
        temp = m[i: i + 1]
        output += basic2[temp]
    return output


if __name__ == '__main__':
    
    m = raw_input("请输入明文:")
    mode = input("选择加密方式 1 or 2：")
    l = []
    k = []
    for i in xrange(len(m)):
        l.append(m[:1])
        m = m[1:]
    if mode == 1:
        for i in l:
            if i.isupper():
                k.append(bec1(i))
            else:
                i = i.upper()
                k.append(bec1(i))

    elif mode == 2:
        for i in l:
            if i.isupper():
                k.append(bec2(i))
            else:
                i = i.upper()
                k.append(bec2(i))
    boom = ''
    for i in k:
        boom += i
    print boom

    

    
