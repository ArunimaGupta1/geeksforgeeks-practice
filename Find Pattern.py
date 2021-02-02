# geeksforgeeks-practice
#User function Template for python3


def findPattern(s,p):
    i=s.find(p)
    return i


#{ 
#Driver Code Starts.




def main():
    t=int(input())
    while(t>0):
        s=input()
        p=input()
        print(findPattern(s,p))
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
