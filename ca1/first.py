import math


def break_arr(arr, key_string):
    n = len(arr)
    mid = math.floor(n/2)
    if(n == 1):
        return arr[0]
    left = []
    right = []
    result = []
    useful_key = key_string[-(n-1):]
    j = 1
    for i in reversed(useful_key):
        if (i == '2'):
            right.insert(0, arr[n-1-j])
        else:
            left.insert(0, arr[n-1-j])
        j += 1
    if (n % 2 == 0):
        if (len(right) < len(left)):
            right.append(arr[n-1])
        else:
            left.append(arr[n-1])
    else:
        if(len(left) == 2):
            right.append(arr[n-1])
        else:
            left.append(arr[n-1])

    new_key = key_string[0:-(n-1)+1]
    left_key = new_key[0:(len(left) - 1)]
    right_key = new_key[(len(left) - 1):]
    result.append(break_arr(left, left_key))
    result.append(break_arr(right, right_key))
    return result


def checksum(arr):
    result = 1
    for i in range(len(arr)):
        result = (31 * result + arr[i]) % 1000003
    return result


n = int(input())
key = input()
arr = list(range(n+1))
arr.pop(0)
result = []
out = break_arr(arr, key)
for ar in out:
    if(isinstance(ar, list)):
        for i in ar:
            result.append(i)
    else:
        result.append(ar)

print(out)
