import math


def recursive_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + recursive_sum(array[1:])


def iterative_sum(array):
    x = 0
    for i in array:
        x += i
    return x


array = [4, 6, 7, 2, 6]

print(f"Sum of array: {recursive_sum(array)}")
print(f"Sum of array: {iterative_sum(array)}")
print(f"Sum of array: {math.fsum(array)}")

# When comparing the efficiency, the library solution is the most effective because it uses the least amount of code
# and is optimized, therefore providing the fastest execution times. The recursive solution is the least efficient
# because of the large number of function calls, while the iterative solution has the most lines of code. The time
# complexity of all three solutions is linear.
