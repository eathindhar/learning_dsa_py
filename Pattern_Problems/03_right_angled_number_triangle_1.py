""""

3. 03_right_angled_number_triangle_1.py
	1
	12
	123
	1234
	12345

"""

def print_right_angled_number_triangle_1_alt(n):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1,end="")
        print("")


# more efficient way would be:

def print_right_angled_number_triangle_1(n):
    for i in range(1, n + 1):
        print(*range(1, i + 1), sep="")

n = int(input())
print_right_angled_number_triangle_1(n)