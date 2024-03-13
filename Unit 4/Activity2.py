import math


def calc_fall_time(distance):
    gravity = 32.1740
    time = math.sqrt(2 * distance / gravity)
    return round(time, 1)


def calc_multiple_fall_times(distances):
    times = []
    for distance in distances:
        time = calc_fall_time(distance)
        times.append(time)
    return times


input_distances = input("Enter distances in feet, separate using spaces")
distances = [float(d) for d in input_distances.split()]

fall_times = calc_multiple_fall_times(distances)

for i, time in enumerate(fall_times):
    print(f"Time for distance {distances[i]} feet is {time} seconds")

total_time = sum(fall_times)
print(f"Total time for all to drop is {total_time}")
