# geeksforgeeks-practice
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def countDistinct(numbers):

    s=set(numbers)
    l=len(s)
    return(l)

#{ 
#Driver Code Starts.

if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers = numbers=[int(x) for x in input().strip().split()]

        
        ans = countDistinct(numbers)
        print(ans)
#} Driver Code Ends
