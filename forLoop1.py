
def utility():
    n=int(input())
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11,1): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*n, end=" ") ## Separating by spaces using end =" "
        



#{ 
#Driver Code Starts.


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        utility()
        print() # To give new line
        testcases-=1
        


if __name__=='__main__':
    main()
#} 