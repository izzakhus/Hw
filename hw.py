def numbers(n):
    for i in range(n + 1):
        if i % 7 == 0:
            if i % 7 == 0:
                yield i

n = 100
for num in numbers(n):
    print(num)