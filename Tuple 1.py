# geeksforgeeks-practice
#{ 
#Driver Code Starts


 # } Driver Code Ends

#User function Template for python3

def doubleTup(numbers):

   l=[]
   for e in numbers:
       l.append(2*e)
   return tuple(l)

#{ 
#Driver Code Starts.
if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers =tuple([int(x) for x in input().strip().split()])
        
        ans = doubleTup(numbers)
        
        if type(ans) != tuple:
            print('your ans is not tuple')
        else:
            print(*ans)
#} Driver Code Ends
