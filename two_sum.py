nums = [2,7,11,15]
target = 9
n = len(nums)
count = 0
for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        else: 
            tar = nums[i] + nums[j]
        if target == tar and count == 0:
            print(f'{i}, {j}')
            count +=1
            break
