import cmath

def solve_quadratic_equation(a, b, c):
    delta = (b**2) - 4*(a*c)

    if delta >= 0:  # Вещественные корни
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2
    else: # Комплексные корни
        x1 = (-b - cmath.sqrt(delta)) / (2 * a)
        x2 = (-b + cmath.sqrt(delta)) / (2 * a)
        return x1, x2

if __name__ == "__main__":
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        roots = solve_quadratic_equation(a, b, c)
        print(f"Корни уравнения: {roots}")
    except ValueError:
        print("Ошибка: Введите числовые значения для коэффициентов.")
    except ZeroDivisionError:
        print("Ошибка: Коэффициент 'a' не может быть равен нулю.")