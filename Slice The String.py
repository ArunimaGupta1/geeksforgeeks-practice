# geeksforgeeks-practice
#User function Template for python3

def sliceString(s):
    #Write your code below
     txt=""
     l=len(s)
     return s[1:l-1:1]



#{ 
#Driver Code Starts.




def main():
    t=int(input())
    while(t>0):
        s=input()
        print(sliceString(s))
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
