from math import factorial

n: int = int(input())

# num: int = 1
# while True:
#     divisible = True
#     for i in range(1, n + 1):
#         if num % i != 0:
#             divisible = False
#             break
#     if divisible:
#         break
#     num += 1
#
# print(num)

# ------------------

num = n
while True:

    for i in range(1, n + 1):
        if num % i != 0:
            break
    else:
        print(num)
        break
    num += n

    num_fact = factorial(n)
    if num > num_fact:
        print('Число не найдено!')
        break
