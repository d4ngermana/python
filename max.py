ar = [2,3,5,7,10,30,22,1,7,8]
max = ar[0]
n = len(ar)
for i in range(1, n):
    if ar[i] > max:
        max = ar[i]
print(f"largest number is {max}")