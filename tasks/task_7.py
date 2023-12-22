print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player1_name: str = input("Игрок 1, введите свое имя: ")
player2_name: str = input("Игрок 2, введите свое имя: ")
repeat: str = "да"

winner: str = "Поздравляем! Победитель - "

att_start: str = "ПРЕДУПРЕЖДЕНИЕ:"
att_end: str = "соблюдайте правила игры. Начнем игру заново!"

ROCK = "камень"
PAPER = "бумага"
SCISSORS = "ножницы"

while repeat == "да":
    player1_choice: str = input(f"{player1_name}: ")
    player2_choice: str = input(f"{player2_name}: ")

    if (player1_choice not in [ROCK, PAPER, SCISSORS] and player2_choice
            not in [ROCK, PAPER, SCISSORS]):
        print(att_start, "Пожалуйста", att_end)
    elif player1_choice not in [ROCK, PAPER, SCISSORS]:
        print(att_start, player1_name, att_end)
    elif player2_choice not in [ROCK, PAPER, SCISSORS]:
        print(att_start, player2_name, att_end)
    else:
        if player1_choice == player2_choice:
            print("Ничья!")
        elif player1_choice == ROCK:
            if player2_choice == SCISSORS:
                print(winner, player1_name)
            elif player2_choice == PAPER:
                print(winner, player2_name)
        elif player1_choice == SCISSORS:
            if player2_choice == PAPER:
                print(winner, player1_name)
            elif player2_choice == ROCK:
                print(winner, player2_name)
        elif player1_choice == PAPER:
            if player2_choice == ROCK:
                print(winner, player1_name)
            elif player2_choice == SCISSORS:
                print(winner, player2_name)

    repeat = input("Хотите продолжить игру? (да/нет): ")

print("До встречи!")
