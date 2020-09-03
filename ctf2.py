string = '0xc4115 0x4cf8'

A = int(string.split(' ')[0], 16)
B = int(string.split(' ')[1], 16)

print(hex(A ^ B))
