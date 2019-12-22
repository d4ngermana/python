my_list = ["geeks", "for", "geeks"]
count = 0
word = input()
N = int(input())
for i in range(0,len(my_list)):
    if my_list[i] == word:
        count += 1
        if count == N:
            del(my_list[i])
        else: 
            print("Wrong Input")

print(my_list)