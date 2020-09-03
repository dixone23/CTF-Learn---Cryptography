string = '41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D'
string_list = string.split(' ')
# #print(string_list)

# flag = []

# for elem in string_list:
#     if elem.isnumeric() == True:
#         if str(elem) == '<0x1f>':
#             flag.append(31)
#         else:
#             n = int(elem)
#             print(chr(n))
#             flag.append(chr(n))

#     elif elem.isnumeric() == False:
#         h = int(elem, 16)
#         print(chr(h))
#         flag.append(chr(h))

# s = ''
# #print(s.join(flag))

def decode(element):
    try:
        try:
            if element == '\x1f':
                element = 31
            return chr(int(element))
        except:
            return(chr(int(element, 16)))

    except Exception as e:
        print(f"Error {e} for {element}")
        pass

decoded = []

for elem in string_list:
    decoded.append(decode(elem))

print(decoded)
