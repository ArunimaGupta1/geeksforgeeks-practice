# geeksforgeeks-practice
def gcd(a, b):
    if a<b:
        small=a
    else:
        small=b
    for x in range(1,small+1):
        if ((a%x==0) and (b%x==0)):
         g=x
    return g
