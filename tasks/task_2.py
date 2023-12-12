numbers: list = ["21", "85", "150", "190", "135", "515", "80"]

for i in numbers:
    i = int(i)

    if i % 5 == 0:
        if i > 500:
            break
        elif i > 150:
            continue

        print(i)
