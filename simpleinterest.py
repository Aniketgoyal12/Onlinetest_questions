def simple_interest(p,r,t):
    amount = p + ((p*r*t)//100)
    return amount

p,r,t = map(int,input("Enter the principle,rate and time").split())
print(simple_interest(p,r,t))