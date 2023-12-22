n: int = int(input("Введите число: "))

if n < 1:
    print(f"Число должно быть больше нуля")
else:
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            print(f"Число {n} не является простым числом")
            break
    else:
        print(f"Число {n} является простым числом")
