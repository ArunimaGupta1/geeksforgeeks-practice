# geeksforgeeks-practice

#User function Template for python3

def alphabets(c1,c2):
    
    i=ord(c1)
    j=ord(c2)
    for x in range(i,j+1):
        print(chr(x),end=" ")
    


#{ 
#Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        c1 = input()
        c2 = input()
        
        alphabets(c1,c2)
        print() #This provides new line
#} Driver Code Ends
