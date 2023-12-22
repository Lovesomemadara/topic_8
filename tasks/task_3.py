n: int = int(input())

range_sum: int = 0
for i in range(1, n + 1):
    range_sum += i

    if range_sum > 100:
        print(f"Сумма всех чисел в диапазоне от 1 до {n} больше 100")
        break
else:
    print(range_sum)
