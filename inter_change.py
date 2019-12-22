arr = [12,35,9,56,24]
n = len(arr)
temp = []
temp = arr[0]
arr[0] = arr[n-1]
arr[n-1] = temp

print(arr)