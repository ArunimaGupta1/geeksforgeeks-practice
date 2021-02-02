# geeksforgeeks-practice
 #{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def sequence(numbers):
  l=[]
  k=list(numbers)
  n=len(k)
  a=k[0]
  d=k[1]-k[0]
  for x in numbers:
      l.append(x)
  m1=k[n-1]+d
  m2=m1+d
  m3=m2+d
  l.append(m1)
  l.append(m2)
  l.append(m3)
  return tuple(l)


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers =tuple([int(x) for x in input().strip().split()])
        
        ans = sequence(numbers)
        
        if type(ans) != tuple:
            print('your ans is not tuple')
        else:
            print(*ans)

#} Driver Code Ends
