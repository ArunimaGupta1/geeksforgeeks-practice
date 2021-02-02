# geeksforgeeks-practice
#User function Template for python3

def posAverage(numbers):
    
   sum=0
   c=0
   l=len(numbers)
   for x in range(0,l):
       if numbers[x]>=0:
           sum=sum+numbers[x]
           c=c+1
   avg=sum/c
   return(avg)
    
