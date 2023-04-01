n = int(input("Enter the size of the triangle: "))

if n <= 0:
    print("Size must be a positive integer.")
else:
    for i in range (1,n): print('*'*(i))
    print("*"*(n+1))
    for j in range (1,n):print('*'*(n-j))

'''
n = 6
*
**
***
****
*****
*******
*****
****
***
**
*
'''
           
        
        
        

        