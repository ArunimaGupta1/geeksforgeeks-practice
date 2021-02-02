# geeksforgeeks-practice
#User function Template for python3

def evenOdd(numbers):
    even = []
    odd = []
    
    for x in range(0,len(numbers)):
        if numbers[x]%2==0:
            even.append(numbers[x])
        else:
            odd.append(numbers[x])
    
    
    return (even,odd) #This is the return statement


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    
    t= int(input())
    
    for _ in range(t):
        
        numbers = numbers=[int(x) for x in input().strip().split()]

        
        even,odd = evenOdd(numbers)
        
        print(*even)
        print(*odd)
#} Driver Code Ends
