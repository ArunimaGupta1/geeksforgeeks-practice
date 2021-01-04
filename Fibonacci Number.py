# geeksforgeeks-practice
def fibonacci(n):
    
    a=1
    b=1
    c=0
    if n==1 or n==2:
       c=1
    else:
        for x in range(n-2):
          c=a+b
          a=b
          b=c
      
    return (c)
