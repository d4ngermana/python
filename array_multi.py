arr = [100,10,5,25,35,14]
n = len(arr)
mul = 1
div = int(input())
for i in range(n):
    mul = (mul * (arr[i] % div)) % div
print(mul) 