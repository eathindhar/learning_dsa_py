"""
Example 1:
Input: word =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: word = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
"""

input_str = input().strip()

# non recursive function
def is_palindrome(word):
    if len(word) == 0:
        return "Not Valid String"
    elif len(word) == 1:
        return "Palindrome"
    else:
        n = len(word)
        for i in range(0,n):
            if i<=int(n/2):
                if word[i] == word[n-1-i] :
                    continue
                else:
                    return "Not Palindrome"    
            return "Palindrome"


#print(is_palindrome(input_str))

#recursive function:
def is_palindrome_recursive(word, left =0, right =None):
    if right is None:
        right = len(word) - 1
    if left >= right:
        return True
    
    if word[left] != word[right]:
        return False

    return is_palindrome_recursive(word,left+1, right - 1)

if is_palindrome_recursive(input_str):
    print(f"{input_str} is Palindrome")
else:
    print(f"{input_str} is Not Palindrome")

"""
madam
01234

0 = 5-1-0

"""