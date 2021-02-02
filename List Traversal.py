# geeksforgeeks-practice
#User function Template for python3

def listTraversal(numbers):
    #Write your code below
    for x in numbers:
        print(x,end=" ")
    
    
    #Don't provide the new line


#{ 
#Driver Code Starts.



    
def main():
    t=int(input())
    
    while(t>0):
        
        numbers=[int(x) for x in input().strip().split()]
        
        listTraversal(numbers)
        print() #Newline by the driver code
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
