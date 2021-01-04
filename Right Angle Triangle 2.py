# geeksforgeeks-practice
def triangle(s):
   
    s=int (s)
    for i in range(s):
        if i == 0 :
            print('*')
    
            
        elif i == s-1:
            print('* '*s)
            
            
        else:
            print('*',' '*(2*(i-1)),'*')
