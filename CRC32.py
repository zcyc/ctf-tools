import binascii
flag = 0x4D1FAE0B
for year in range(1500,2500):
    for mon in range(1,10):
        for day in range(1,10):
            a = str(year)+'0'+str(mon)+'0'+str(day)
            b= binascii.crc32(a)
            if b == flag:
                print a