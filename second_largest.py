my_list = [8,7,6,5,4]
n = len(my_list)
largest = my_list[1]   #57
sec = my_list[0]      #57
for i in range(n):
    if my_list[i] == largest:
        continue
    elif my_list[i] > largest:   #8>7
        sec = largest #sec=7
        largest = my_list[i] #largest=8
    elif my_list[i] > sec: 
        sec = my_list[i]
    elif my_list == sec or my_list[i] < largest:  # 7<8
        sec = my_list[i] #sec=7
print(sec)
