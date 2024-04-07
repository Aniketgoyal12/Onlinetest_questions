name = ''
ascii_value = input().split('&')
name = ''.join(chr(int(value)) for value in ascii_value)
print(name)
