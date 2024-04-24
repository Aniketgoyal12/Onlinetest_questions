name = input()
index = name.find(" ",0)
code_name = name[index-1].upper() + name[index+1]
print(code_name)