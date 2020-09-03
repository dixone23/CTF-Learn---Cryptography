s = '''q{vpln'bH_varHuebcrqxetrHOXEj'''

char_list = []
for c in s:
    char_list.append(c)

outs = []

for i in range(256):
#for i in range(23, 24):
    for j in range(0, len(char_list)):
        try:
            outs.append(ord(char_list[j]) ^ i)
        except:
            pass

decoded = [chr(k) for k in outs]
a = ''
print(a.join(decoded))
