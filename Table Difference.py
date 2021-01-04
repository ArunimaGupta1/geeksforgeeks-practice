# geeksforgeeks-practice
#User function Template for python3

def difference(n1,n2):
    
    #Complete the code below
    for i in range( 1,11 ):
        print((n1-n2)*i ,end=' ')
    


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        #Taking the input in a single line
        n1,n2 =map(int,input().split())
        
        difference(n1,n2)
        #The below code provides a new line
        print()
        
    
#} Driver Code Ends
