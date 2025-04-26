""""

6. 06_right_angled_inverted_number_triangle.py
	12345
	1234
	123
	12
	1

"""

n = int(input())
num_str = ""
for i in range(1,n+1):
    k = 1
    for j in range(0,n+1-i):
        num_str = num_str+str(k)
        k = k+1
    print(num_str)
    num_str=""