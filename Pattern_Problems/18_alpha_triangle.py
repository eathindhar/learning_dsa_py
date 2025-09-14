""""

18. 18_alpha_triangle.py
    F
    E F
    D E F
    C D E F
    B C D E F
    A B C D E F

"""

print("Program Started")
n = int(input())
num_str = ""
count = ord("A")
for i in range(n,0,-1):
    num_str = num_str+chr(count+i-1)+" "
    print(num_str[::-1])

# Alternate
ans = 64 + n
for i in range(n): 
    for j in range(i+1):
        print(chr(ans - j), end = ' ')
    ans = 64 + n
    print()

print("Program Completed")