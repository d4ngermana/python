x = int(input())
n = 0
arm = 0
temp = x
temp2 = x
while x!=0:
    n+=1
    x = int(x/10)
while temp!=0:
    y = temp%10
    arm = arm + (y**n)
    temp = int(temp/10)

if temp2 == arm : 
    print(f"{arm} is a Armstrong Number")
else: 
    print(f"{arm} is not Armstrong Number")

