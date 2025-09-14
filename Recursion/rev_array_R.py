"""
Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""

n = int(input())
arr = []
test_arr = [1]+[2]+[3]+[4]+[5]
for i in range(0,n):
    arr.append(int(input()))

def rev_array(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + rev_array(arr[:-1])

arr = rev_array(arr)

print("input: ",n," output : ",arr)
print("test output : ",test_arr)

"""
arr = 1,2,3,4,5
arr[-1] = 5 + 
arr[:-1] = 1,2,3,4
rev_array(1,2,3,4)
arr = 4 + rev_array(1,2,3)
arr = 3 + rev_array(1,2)
arr = 2 + rev_array(1)
arr = 1 + rev_array()
arr = []
return []

[5] + rev([1,2,3,4])
[5] + [4] + rev([1,2,3])
[5] + [4] + [3] + rev([1,2])
[5] + [4] + [3] + [2] + rev([1])
[5] + [4] + [3] + [2] + [1] + rev([])
[5] + [4] + [3] + [2] + [1] + []
[5,4,3,2,1]

"""