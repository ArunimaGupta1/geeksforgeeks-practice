# geeksforgeeks-practice
def nextPrime(n):
    while True:
        n=n+1
        flag = 0 
        for i in range(2,n):
            if n%i==0:
               flag = 1
               break
        if flag == 0:
            return(n)
