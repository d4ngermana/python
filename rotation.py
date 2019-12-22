ar = [1,2,3,4,5,6,7]
rotate = int(input("How many rotation?"))
n = len(ar)
while rotate:
    temp = ar[0]
    for i in range(n-1):
        ar[i] = ar[i+1]
    ar[n-1] = temp
    rotate-=1
print(ar) 
