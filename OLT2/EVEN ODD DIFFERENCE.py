def differende_even_odd(num1):
    string_num = str(num1)
    sum_odd = 0
    sum_even = 0
    for i in range(len(string_num)):
        if i%2 == 0:
            sum_even += int(string_num[i])
        else:
            sum_odd += int(string_num[i])
    isodd = False
    difference = sum_even - sum_odd
    if difference % 2 == 0:
        isodd = True
    else:
        isodd = False
    return isodd
num1 = int(input())
print(differende_even_odd(num1))