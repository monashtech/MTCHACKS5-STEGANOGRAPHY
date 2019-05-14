import os
import sys


if __name__ == "__main__":
    filename = sys.argv[1]
    hidename = sys.argv[2]
    with open(filename, 'rb') as file:
        data = file.read()
    file.close()
    with open(hidename, "rb") as file2:
        data2 = file2.read()
    file2.close()

    signature = bytearray(b'\xff\xAF\xAF\xAF')
    barr = bytearray(data)
    barr += signature
    barr += bytearray(data2)
    
    with open("final.png", "wb") as out:
        out.write(bytes(barr))
    out.close()