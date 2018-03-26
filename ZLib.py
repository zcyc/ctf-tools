from PIL import Image
from zlib import *

data = open('图片名', 'rb').read()[0x15AFFB:]
data = decompress(data)

img = Image.new('1', (25, 25))
d = img.load()

for n, i in enumerate(data):
    d[(n % 25, n / 25)] = int(i) * 255

f = open('flag.png', 'wb')
img.save(f)