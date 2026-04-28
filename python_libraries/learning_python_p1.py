import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


def length_of_strings(str):
    cnt = 0
    for element in str:
        cnt = cnt + 1
    return cnt

name = "Eathindhar"
print(len(name))
print(length_of_strings(name))