file = open('data.txt', 'r')
data = file.read()

print("raw data:")
print(data)

decoded = ""
word = ""
i = 0

print("decoded data:")

while i < len(data)-1:
    if data[i] == '1':
        if data[i:i+8] == '11000000':
            decoded += "0"
            i+=8
        elif data[i:i+8] == '11100000':
            decoded += "0"
            i+=8
        elif data[i:i+8] == '11110000':
            decoded += "0"
            i+=8
        elif data[i:i+8] == '11111000':
            decoded += "1"
            i+=8
        elif data[i:i+8] == '11111100':
            decoded += "1"
            i+=8
        elif data[i:i+8] == '11111110':
            decoded += "1"
            i+=8
        elif data[i:i+8] == '11111111':
            decoded += "1"
            i+=8

    elif data[i] == '0':
        if data[i:i+40] == '0000000000000000000000000000000000000001':
            if len(decoded) > 0:
                num = int(decoded[:-1], 2)
                print("end of transmiting byte:")
                print(num, chr(num))
                word += chr(num)
                decoded = ""
        elif data[i:i+14] == '00000000000001':
            if len(decoded) > 0:
                num = int(decoded[:-1], 2)
                print(decoded, num)
            if len(decoded) == 13:
                print("end of one iteration")
                i+=13
            decoded = ""
        elif i == len(data)-2 :
            if len(decoded) > 0:
                num = int(decoded[:-1], 2)
            print("end of transmiting byte:")
            print(num, chr(num))
            word += chr(num)
            print("----------------------------")
            print("end of transmition, message:")
            print(word)
            print("----------------------------")

    i+=1
