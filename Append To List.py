# geeksforgeeks-practice
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def appendToList(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    return(l)


#{ 
#Driver Code Starts.



    
def main():
    t=int(input())
    
    while(t>0):
        
        a=int(input())
        b=int(input())
        c=int(input())
        
        for x in (appendToList(a,b,c)):
            print(x,end=" ")
        print()
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends
