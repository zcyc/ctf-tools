#coding=utf-8
def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+97)] = chr(i+97)
    return pwd_dic
if __name__ == '__main__':
    pwd_dic = {}
    pwd = "sjoyuxzr"    #要解密的内容
    plain = []    
    pwd_dic = affine(11, 8)     #仿射函数参数
    for i in pwd:        
        plain.append(pwd_dic[i])    
    print "You Flag is: " + "".join(plain)