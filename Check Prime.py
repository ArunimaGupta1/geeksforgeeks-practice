# geeksforgeeks-practice
def prime(n):
    
    c=0
    if n==1:
        return False
    else:
        for i in range(1,n+1):
            if n%i==0:
              c=c+1
    if c==2:
        return True
    else:
        return False
