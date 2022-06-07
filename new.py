import math


def decision(a, b, c):
    discr = b ** 2 - 4 * a * c
    return "Дискриминант D = %.2f" % discr
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return ("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        return ("x = %.2f" % x)
    else:
        return ("Корней нет")


print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
