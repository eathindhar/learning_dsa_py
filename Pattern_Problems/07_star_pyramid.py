""""

7. 07_star_pyramid.py
	     *     
	    ***    
	   *****   
	  *******  
	 ********* 
	***********

"""

n = int(input())
num_str = ""
for i in range(0,n):
    num_str = " "*(n-i-1)
    num_str = num_str+("*"*((2*i)+1))
    print(num_str)
    num_str=""