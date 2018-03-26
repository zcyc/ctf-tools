# #coding=utf-8
import hashlib
import random
x = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = ''
def cctv(x):
    x1 = random.choice(x)
    x2 = random.choice(x)
    x3 = random.choice(x)
    x4 = random.choice(x)
    global m
    m = 'gctf(H%sn5%s1sw%s1%sV)'%(x1, x2, x3, x4)   #明文
    m1 = hashlib.md5(m.encode('utf-8')).hexdigest() #将明文进行md5加密
    return m1

y = str(cctv(x))
z = y[:9]
v = '3c935afab' #已知的部分密文，用作比对结果
print '正在运行，请稍后...'
state=0
while (v!=z):
    y = str(cctv(x))
    z = y[:9]
    if v==z:
        state=1

if state==1:
    print '运算成功，结果为：' + m
else:
    print '无结果！'