# geeksforgeeks-practice
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def decrementList(numbers):
    for x in range(0,len(numbers)):
       numbers[x]=numbers[x]-1
    return(numbers)

#{ 
#Driver Code Starts.



def main():
    t=int(input())
    
    while(t>0):
        
        numbers=[int(x) for x in input().strip().split()]
        
        for x in (decrementList(numbers)):
            print(x,end=" ")
        print()
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
