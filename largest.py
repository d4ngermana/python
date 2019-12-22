my_list = [10,3,24,13,52,5,56,1,3,2]
n = len(my_list)
largest = my_list[0]
for i in range(n):
    if largest < my_list[i]:
        largest = my_list[i]

print(largest)