start: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if start == end or (start < 0 or end < 0):
    print(f"Некорректный диапазон")
else:
    print(f"Простые числа в заданном диапазоне:")
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                print(i, end=' ')
        # else:
        #     print('В заданном диапазоне простых чисел нет.')
