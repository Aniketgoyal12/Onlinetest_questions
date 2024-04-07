def no_chocolate(c,n,d):
    return c + n * (d-1)
c,n,d = map(int,input("Enter the chocolate,no of days,no of chocolates").split())
print(no_chocolate(c,n,d))