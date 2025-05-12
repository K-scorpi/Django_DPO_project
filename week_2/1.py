def is_even_or_odd(number):
    if number % 2 == 0:
        return "четное"
    else:
        return "нечетное"

if __name__ == "__main__":
    try:
        num = int(input("Введите целое число: "))
        result = is_even_or_odd(num)
        print(f"Число {num} {result}.")
    except ValueError:
        print("Ошибка: Введите целое число.")