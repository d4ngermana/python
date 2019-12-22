nums = [2,7,11,15]
target = 9
n = len(nums)
for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        else: 
            tar = nums[i] + nums[j]
            if target == tar:
                print(f'{i}, {j}')