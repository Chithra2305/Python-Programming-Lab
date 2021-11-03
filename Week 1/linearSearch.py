def linearSearch(arr, key):
  for i in range(len(arr)):
    if arr[i] == key:
      return i
    return -1
 
def linearSearch_recur(arr, key, i = 0):
    if arr[i] == key:
        return i
    if i != len(arr) - 1:
        return linearSearch_recur(arr, key, i+1)
    return -1
 
arr = [1, 6 , 78, 765782, 7, 673, 92]
index = linearSearch(arr, 7)
if index == -1:
    print("Element not found")
else:
    print("Element is at index", index)
index = linearSearch_recur(arr, 7)
if index == -1:
    print("Element not found")
else:
    print("Element is at index", index)
