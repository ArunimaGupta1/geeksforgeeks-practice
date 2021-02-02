# geeksforgeeks-practice
#User function Template for python3

def reverseString(s):
  
  return(s[::-1])
    

#{ 
#Driver Code Starts.



def main():
    t=int(input())
    while(t>0):
        s=input()
        print(reverseString(s))
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
