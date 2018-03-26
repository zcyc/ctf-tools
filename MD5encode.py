import hashlib

def md5Encode(str):

    # 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
    m = hashlib.md5(str.encode(encoding='utf-8'))
    return m.hexdigest()

test = open('new.txt','r')
t = open('mdzz.txt','a')
for tmp in test.readlines():
    tmp = ''.join(tmp.split())
    print(md5Encode(tmp))
    t.write(md5Encode(tmp)+'\n')
t.close()
test.close()



