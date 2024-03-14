print("Program Started")
n = int(input())
num_str = ""
for i in range(0,n):
    if i%2!=0:
        num_str = "0"+num_str
    else:
        num_str = "1"+num_str
    print(num_str)

print("Program Completed")