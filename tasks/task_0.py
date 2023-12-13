positive_sum = negative_sum = negative_count = 0

while True:
    num: int = int(input("Введите целое число: "))

    if num < 0:
        negative_count += 1
        negative_sum += num

        if negative_count == 3:
            break
    else:
        positive_sum += num

print("Сумма положительных чисел:", positive_sum)
print("Сумма отрицательных чисел:", negative_sum)
