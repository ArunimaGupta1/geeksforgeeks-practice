# geeksforgeeks-practice
#User function Template for python3

        
# Function to print x in decreasing order
def utility():
    #The line below takes input. Don't chamge it!
    x=int(input())
    
    # Complete the code below
    while(x >= 0):
        print(x,end=" ")
        x=x-1
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code



#{ 
#Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        
        
        utility()
        
        print() #This gives a new line
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} 
