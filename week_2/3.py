def find_maximum(numbers):
    if not numbers:
        return None

    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == "__main__":
    my_list = [1, 5, 2, 8, 3, 9, 4]
    max_value = find_maximum(my_list)
    print(f"Максимальное значение в списке: {max_value}")