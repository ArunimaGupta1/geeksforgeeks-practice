# geeksforgeeks-practice
#User function Template for python3

def listSum(numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    return(sum)    
    
    


#{ 
#Driver Code Starts.



def main():
    t=int(input())
    
    while(t>0):
        
        numbers=[int(x) for x in input().strip().split()]
        
        print(listSum(numbers))
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
