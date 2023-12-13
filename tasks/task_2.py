numbers: list[str] = ["21", "85", "150", "190", "135", "515", "80"]

for i in numbers:
    i = int(i)

    if i > 500:
        break

    if i > 150:
        continue

    if i % 5 == 0:
        print(i)
