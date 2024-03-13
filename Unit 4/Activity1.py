def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        smallest = i
        for j in range(i + 1, size):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


def bubble_sort(array):
    size = len(array)
    for i in range(size - 1):
        for j in range(size - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


array = [6, 7, 4, 8, 12, 9, 5, 3, 14, 11]

selection_sorted_array = selection_sort(array)
bubble_sorted_array = bubble_sort(array)

print(selection_sorted_array)
print(bubble_sorted_array)

search_for = int(input("Enter an integer value to search for"))


def binary_search(array, search_for):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == search_for:
            return mid
        if guess >= search_for:
            high = mid - 1
        else:
            low = mid + 1
    return None


is_present = binary_search(bubble_sorted_array, search_for)

if is_present is not None:
    print(f"{search_for} was found in the list!")
else:
    print(f"{search_for} is not in the list!")
