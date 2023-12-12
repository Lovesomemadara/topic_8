n: int = int(input("Введите число: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"Число {n} не является простым числом")
            break
    else:
        print(f"Число {n} является простым числом")
else:
    print(f"Число должно быть положительным")
