num = int(input())
if num > 1:
    for i in range(2, num//2):
        if(num % i) == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is Prime Number")
else:
    print(f"{num} is not prime")