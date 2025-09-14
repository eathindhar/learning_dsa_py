"""
Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
"""

input_str = input()

# non recursive function
def is_palindrome(str):
    if len(str) == 0:
        return "Not Valid String"
    elif len(str) == 1:
        return "Palindrome"
    else:
        n = len(str)
        for i in range(0,n):
            if i<=int(n/2):
                if str[i] == str[n-1-i] :
                    continue
                else:
                    return "Not Palindrome"    
            return "Palindrome"


print(is_palindrome(input_str))

#recursive function:
def is_palindrome_recursive(str):
    pass

"""
madam
01234

0 = 5-1-0

"""