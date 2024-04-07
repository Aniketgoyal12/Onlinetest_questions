def ant_consensus(c,k,n):
    return c * (k**n)
c,k,n = map(int,input("Enter the no of ants,increment number,no of days").split())
print(ant_consensus(c,k,n))