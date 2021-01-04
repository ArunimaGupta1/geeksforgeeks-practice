Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,11,1)
SyntaxError: invalid syntax
>>> for i in range(1,11,1):
	for j in range(1,11,1):
		print(i,'*',j,'=',i*j,sep=' ')
		print()
		