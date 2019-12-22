num = int(input())
f = 0
s = 1
fib = 0
print(f'First {num} fibonacci series is:')
while fib < num:
    fib = f + s
    f = s
    s = fib
    print(f'{fib}')
