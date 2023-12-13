print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player1_name: str = input("Игрок 1, введите свое имя: ")
player2_name: str = input("Игрок 2, введите свое имя: ")
repeat: str = "да"

rock = "камень"
paper = "бумага"
scissors = "ножницы"

while repeat == "да":

    player1_choice: str = input(f"{player1_name}: ")
    player2_choice: str = input(f"{player2_name}: ")

    if player1_choice == player2_choice:
        print("Ничья!")
    elif player1_choice == "камень":
        if player2_choice == "ножницы":
            print(f"Поздравляем! Победитель - {player1_name}!")
        elif player2_choice == "бумага":
            print(f"Поздравляем! Победитель - {player2_name}!")
    elif player1_choice == "ножницы":
        if player2_choice == "бумага":
            print(f"Поздравляем! Победитель - {player1_name}!")
        elif player2_choice == "камень":
            print(f"Поздравляем! Победитель - {player2_name}!")
    elif player1_choice == "бумага":
        if player2_choice == "камень":
            print(f"Поздравляем! Победитель - {player1_name}!")
        elif player2_choice == "ножницы":
            print(f"Поздравляем! Победитель - {player2_name}!")
    else:
        print("ПРЕДУПРЕЖДЕНИЕ: Макс соблюдайте правила игры. Начнем игру заново!")
        continue

    repeat = input("Хотите продолжить игру? (да/нет): ")

print("До встречи!")
