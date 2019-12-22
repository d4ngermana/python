my_list = [10,12,9,5,35,32]
new_list = []
n = len(my_list)
for i in range(n):
    new_list.append(my_list[n-1-i])

print(new_list)