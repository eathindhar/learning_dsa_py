""""

1. 01_rectangle.py
	*****
	*****
	*****
	*****
	*****

"""

def print_rectangle_1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")


# alternative and a simpler way in python
def print_rectangle_2(n):
    for i in range(n):
        print("*"*n)


# More efficient way would be, this avoids more string operation
def print_rectangle(n):
    line = "*" * n
    for i in range(n):
        print(line)


n = int(input())
print_rectangle(n)