import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, k = line.split(' ')
    k = int(k)
    line = sys.stdin.readline().rstrip()
    houses_array = [int(number) for number in line.split(' ')]
    houses_array.sort()
    houses_counter = 0
    while True:
        if houses_counter == len(houses_array):
            break
        if houses_array[houses_counter] <= k:
            k -= houses_array[houses_counter]
            houses_counter += 1
        else:
            break
    print(houses_counter)


if __name__ == '__main__':
    main()