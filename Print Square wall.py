# geeksforgeeks-practice
#User function Template for python3

def squareWall(s):
   
    for i in range(s):
        for j in range(s):
            print("*",sep=" ",end=" ")
        print()
        
        # complete above print function to print square wall
        
        


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=int(input())
        squareWall(s)
#} Driver Code Ends
