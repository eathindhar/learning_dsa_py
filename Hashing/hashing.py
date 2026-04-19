# Hashing
def num_count(num,arr):
    count = 0
    for i in range(0,len(arr)):
        if num == arr[i]:
            count += 1
    return count

print(num_count(1,[1,2,1,3,2]))


"""
prestoring and fetching


"""

