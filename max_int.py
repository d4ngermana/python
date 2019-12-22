def max_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(max_even([10,1,3,5,11,2,12,14,2,31,33,4]))