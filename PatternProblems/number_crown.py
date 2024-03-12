import time
begin = time.time()
print(f"Program Started at {begin}")

def num_string(n, flag):
    string = ""
    if flag == 0:
        for i in range(1,n+1):
            string = string+str(i)
    else:
        for i in range(n,0,-1):
            string = string+str(i)
    return string

n = int(input())
num_str = ""
for i in range(0,n):
    num_str = num_str+num_string(i+1,0)
    num_str = num_str+" "*((n-i-1)*2)
    num_str = num_str+num_string(i+1,1)
    print(num_str)
    num_str = ""

end = time.time()
print(f"Program Completed at {end}")
print(f"Time taken is {round(end-begin,3)}")
