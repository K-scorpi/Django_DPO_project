import random

def guess_the_number():
    secret_number = random.randint(1, 9)
    attempts_left = 3

    print("Я загадал число от 1 до 9. Попробуй угадать!")

    while attempts_left > 0:
        try:
            guess = int(input(f"Попытка {4 - attempts_left}: Введи число: "))
            if 1 <= guess <= 9: 
                if guess < secret_number:
                    print("Ваше число меньше.")
                elif guess > secret_number:
                    print("Ваше число больше.")
                else:
                    print("Вы угадали!")
                    return  
                attempts_left -= 1

            else:
                print("Введите число от 1 до 9") 
        except ValueError:
            print("Ошибка: Введите целое число.") 

    print(f"Вы проиграли! Я загадал число {secret_number}.")
    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() == "да":
        guess_the_number()

if __name__ == "__main__":
    guess_the_number()