import base64
from PIL import Image

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

with open('somehide.txt', 'r') as hideFile:
    s = hideFile.read()
hideFile.close()

bit_array = tobits(s)
print(bit_array)

im = Image.open("fnatic.png")
im.save("test.png")

im = Image.open("test.png")
width, height = im.size
pixels = im.load()

i = 0
for x in range(0,width):
    r,g,b,a = pixels[x,0]
    #print("[+] Pixel : [%d,%d]"%(x,0))
    #print("[+] \tBefore : (%d,%d,%d)"%(r,g,b))
    #Default values in case no bit has to be modified
    new_bit_red_pixel = 255
    new_bit_green_pixel = 255
    new_bit_blue_pixel = 255

    if i<len(bit_array):
        #Red pixel
        r_bit = bin(r)
        r_new_last_bit = bit_array[i]
        new_bit_red_pixel = int(r_bit[:-1]+str(r_new_last_bit),2)
        i += 1

    if i<len(bit_array):
        #Green pixel
        g_bit = bin(g)
        g_new_last_bit = bit_array[i]
        new_bit_green_pixel = int(g_bit[:-1]+str(g_new_last_bit),2)
        i += 1

    if i<len(bit_array):
        #Blue pixel
        b_bit = bin(b)
        b_new_last_bit = bit_array[i]
        new_bit_blue_pixel = int(b_bit[:-1]+str(b_new_last_bit),2)
        i += 1

    pixels[x,0] = (new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel, a)
    #print("[+] \tAfter: (%d,%d,%d)"%(new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel))

im.save('test.png')


