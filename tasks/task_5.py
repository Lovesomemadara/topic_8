n: int = int(input())

num: int = 1
while True:
    divisible = True
    for i in range(1, n + 1):
        if num % i != 0:
            divisible = False
            break
    if divisible:
        break
    num += 1

print(num)
