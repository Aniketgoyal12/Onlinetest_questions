#Program to calculate compound interest for 2 years
import math
def compound_interest(p,r):
    ci = p*pow((1+r/100),2) - p
    return ci
p,r = map(int,input("enter the principle and rate of interest").split())
print(compound_interest(p,r))