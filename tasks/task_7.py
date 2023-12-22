print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player1_name: str = input("Игрок 1, введите свое имя: ")
player2_name: str = input("Игрок 2, введите свое имя: ")
repeat: str = "да"

winner: str = "Поздравляем! Победитель - "

att_player1: str = (f"ПРЕДУПРЕЖДЕНИЕ: {player1_name} соблюдайте "
                    f"правила игры. Начнем игру заново!")

att_player2: str = (f"ПРЕДУПРЕЖДЕНИЕ: {player2_name} соблюдайте "
                    f"правила игры. Начнем игру заново!")

att_all: str = ("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте правила игры. "
                "Начнем игру заново!")

game: list = ["бумага", "камень", "ножницы"]

while repeat == "да":

    player1_choice: str = input(f"{player1_name}: ")
    player2_choice: str = input(f"{player2_name}: ")

    if player1_choice not in game and player2_choice not in game:
        print(att_all)
    elif player1_choice not in game:
        print(att_player1)
    elif player2_choice not in game:
        print(att_player2)
    else:
        if ((player1_choice and player2_choice) in game
                and player1_choice == player2_choice):
            print("Ничья!")
        elif player1_choice == game[1]:
            if player2_choice == game[2]:
                print(winner, player1_name)
            elif player2_choice == game[0]:
                print(winner, player2_name)
        elif player1_choice == game[2]:
            if player2_choice == game[0]:
                print(winner, player1_name)
            elif player2_choice == game[1]:
                print(winner, player2_name)
        elif player1_choice == game[0]:
            if player2_choice == game[1]:
                print(winner, player1_name)
            elif player2_choice == game[2]:
                print(winner, player2_name)

    repeat = input("Хотите продолжить игру? (да/нет): ")

print("До встречи!")
