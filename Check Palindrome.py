# geeksforgeeks-practice
#User function Template for python3



def isPalin(s):
    s=s.lower()
    if s==s[::-1]:
        return("True")
    else:
        return("False")

#{ 
#Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        s=input()
        print(isPalin(s))
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
