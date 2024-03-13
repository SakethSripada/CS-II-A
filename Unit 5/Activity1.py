import math


def difference_of_squares(a, b, y=None):
    if y is None:
        r1 = f"({math.sqrt(a)}x - {math.sqrt(b)})"
        r2 = f"({math.sqrt(a)}x + {math.sqrt(b)})"
        print(f"The factored form is: {r1}{r2}")
    else:
        r1 = f"({math.sqrt(a)}x - {math.sqrt(b)}{y})"
        r2 = f"({math.sqrt(a)}x + {math.sqrt(b)}{y})"
        print(f"The factored form is: {r1}{r2}")


a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
y = input("If your quadratic is of form ax^2 - by^2, enter the name of variable y.")

difference_of_squares(a, b, y if y != " " else None)
