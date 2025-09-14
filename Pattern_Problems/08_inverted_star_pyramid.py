""""

8. 09_inverted_star_pyramid.py
	***********
	 *********
	  *******
	   ***** 
	    ***    
	     *

"""

print("Program Started")
n = int(input())
num_str = ""
for i in range(n,0,-1):
    num_str = num_str + " "*(n-i)
    num_str =  num_str+"*"*((i-1)*2+1)
    print(num_str)
    num_str=""

print("Program Completed")
