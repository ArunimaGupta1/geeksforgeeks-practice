# geeksforgeeks-practice
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def lessThan(numbers,k):
    ans=[]
    l=len(numbers)
    for x in range(0,l):
        if numbers[x]<k:
            ans.append(numbers[x])
    return (ans)
    # write your code below to append all numbers to ans which are less than k
    
    return ans


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers = numbers=[int(x) for x in input().strip().split()]
        k = int(input())
        
        ans = lessThan(numbers,k)
        print(*ans)
#} Driver Code Ends
