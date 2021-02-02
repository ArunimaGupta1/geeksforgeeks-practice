# geeksforgeeks-practice
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def listTraversalReverse(numbers):
    #Write your code below
    l=len(numbers)
    for x in range(l-1,-1,-1):
        print(numbers[x],end=" ")
    
    
    #Don't add a new line as it is provided by the driver code


#{ 
#Driver Code Starts.



    
def main():
    t=int(input())
    
    while(t>0):
        
        numbers=[int(x) for x in input().strip().split()]
        
        listTraversalReverse(numbers)
        print() #New line
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
