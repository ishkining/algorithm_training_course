n = int(input())
houses_array = [int(number) for number in input().split(' ')]

distance_array = [0] * n

if houses_array[0] == 0:
    distance_array[0] = 0
else:
    distance_array[0] = (10**6) + 1

for house_index in range(1, len(houses_array)):
    if houses_array[house_index] == 0:
        distance_array[house_index] = 0
    else:
        distance_array[house_index] = distance_array[house_index - 1] + 1

print(distance_array)

for house_index in range(len(houses_array) - 2, -1, -1):
    if houses_array[house_index] != 0:
        distance_array[house_index] = min(distance_array[house_index], distance_array[house_index + 1] + 1)

print(distance_array)