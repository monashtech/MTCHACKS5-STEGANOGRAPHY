import os
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "rb") as readFile:
        data = readFile.read()
    readFile.close()
    data = bytearray(data)
    signature = bytearray(b'\xff\xAF\xAF\xAF')

    offset = 0
    for d in range(len(data)):
        if data[d] == signature[0] and data[d+1] == signature[1] and data[d+2] == signature[2] and data[d+3] == signature[3]:
            offset = d+4
            break

    result = bytes(data[offset:])
    finalStr = result.decode()
    finalfile = "output.txt"
    with open(finalfile, "w") as outFile:
        outFile.write(finalStr)
    outFile.close()