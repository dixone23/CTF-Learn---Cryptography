string = '41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D'
string_list = string.split(' ')

def decode(element):
    try:
        return chr(int(element, 16))

    except Exception as e:
        print(f"Error {e} for {element}")
        pass

decoded = []

for elem in string_list:
    decoded.append(decode(elem))

s = ''
print(f'FLAG = {s.join(decoded)}')
