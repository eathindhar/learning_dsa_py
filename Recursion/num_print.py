n = int(input())

count = 0 
def func(n,i):
    if i > n:
        return
    print(i)
    i += 1
    func(n,i)


func(n,1)