"""
Given an array of integers: 
[1, 2, 1, 3, 2] and we are given some 
queries: [1, 3, 4, 2, 10]. 
For each query, we need to find out how many times the number appears in the array. 
For example, if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0. 
"""


def find_number(n,arr):
    count = 0
    for i in range(0,len(arr)):
        if n == arr[i]:
            count +=1
    return count

arr = [1,2,1,3,2]
query = [1,3,4,2,10]

for i in range(0,len(query)):
    print(query[i],find_number(query[i],arr))