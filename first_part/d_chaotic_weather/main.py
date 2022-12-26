n = int(input())
degrees_array = [int(number) for number in input().split(' ')]
chaos_counter = 0
for degree_index in range(len(degrees_array)):
    if (degree_index == 0 or degrees_array[degree_index] > degrees_array[degree_index - 1]) and \
            (degree_index == len(degrees_array) - 1 or degrees_array[degree_index] > degrees_array[degree_index + 1]):
        chaos_counter += 1

print(chaos_counter)