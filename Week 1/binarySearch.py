def binarySearch(arr, key):
    n = len(arr) // 2
    while n > 0 and n < len(arr):
        if arr[n] == key:
            return n
        elif arr[n] > key:
            n = n // 2
            if n > n * 2:
                return -1
        else:
            n = n + n // 2
            if n < n - n // 2:
                return -1
    return -1


def binarySearch_recur(arr, key, n = None):
    if n == None:
        n = len(arr) // 2
    if arr[n] == key:
        return n
    boundary = n > 0 and n < len(arr)
    if boundary:
        if arr[n] > key:
            if n > n * 2:
                return -1
            return binarySearch_recur(arr, key, n// 2)
        else:
            if n < n - n // 2:
                return - 1
            return binarySearch_recur(arr, key, n + n // 2)
    return -1

arr = [1, 96, 7, 8, 76]
arr.sort()
print(binarySearch(arr, 6))
print(binarySearch_recur(arr, 9, len(arr) // 2))

