def fibonacci(n):
    a = 0
    b = 1
    list = [a, b]

    for i in range(n - 2):
        fib = a + b
        a = b
        b = fib
        list.append(fib)
    return list


def binary(number):
    if number == 0:
        return "0"
    list = []
    while number > 0:
        list.append(str(number % 2))
        number = number // 2
    list.reverse()
    return " ".join(list)


n = int(input("How many fibonacci numbers would you like?"))

result = fibonacci(n)
binary = [binary(number) for number in result]
print(f"First {n} fibonacci numbers are: {result}")
print(f"First {n} fibonacci numbers in binary: {binary}")
