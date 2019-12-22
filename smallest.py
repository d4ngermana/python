my_list = [10,20,4,6,83,2,6]
n = len(my_list)
small = my_list[0]
for i in range(n):
    if small > my_list[i]:
        small = my_list[i]

print(small)