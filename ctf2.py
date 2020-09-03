string = '0xc4115 0x4cf8'

def decode(s):
    for elem in s.split(' '):
        d = int(elem, 16)
        print(chr(d), d)

decode(string)
