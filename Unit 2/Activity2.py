def grade(points):
    global result
    if points >= 90:
        result = "A"
    elif points >= 80:
        result = "B"
    elif points >= 60:
        result = "C"
    elif points >= 50:
        result = "D"
    else:
        result = "F"
    return result

score = int(input("How many points did you get on the assignment, out of 100?"))
grade(score)
print(result)