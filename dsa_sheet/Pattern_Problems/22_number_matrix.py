""""

22. 22_number_matrix.py
    6 6 6 6 6 6 6 6 6 6 6 
    6 5 5 5 5 5 5 5 5 5 6 
    6 5 4 4 4 4 4 4 4 5 6 
    6 5 4 3 3 3 3 3 4 5 6 
    6 5 4 3 2 2 2 3 4 5 6 
    6 5 4 3 2 1 2 3 4 5 6 
    6 5 4 3 2 2 2 3 4 5 6 
    6 5 4 3 3 3 3 3 4 5 6 
    6 5 4 4 4 4 4 4 4 5 6 
    6 5 5 5 5 5 5 5 5 5 6 
    6 6 6 6 6 6 6 6 6 6 6

"""

print("Program Started")
n = int(input())
rows = cols = 2*n-1
num_str = ""
matrix = [[0 for j in range(cols)] for i in range(rows)]
mid = n
for i in range(rows):
    for j in range(cols):
        top = i
        bottom = j
        right = (2*n-2) - j
        left = (2*n-2) - i
        print(f'{n - min(min(top,bottom),min(left,right)):02}',end = " ")
    print("")

print("Program Completed")