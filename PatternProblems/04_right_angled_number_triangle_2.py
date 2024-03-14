def print_right_angled_number_triangle_2(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print("")


n = int(input())
print_right_angled_number_triangle_2(n)