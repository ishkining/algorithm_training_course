import sys


def main():
    n = int(input())
    m = int(input())
    line = sys.stdin.readline().rstrip()
    north_array = [int(number) for number in line.split(' ')]
    line = sys.stdin.readline().rstrip()
    south_array = [int(number) for number in line.split(' ')]
    result = None
    while len(north_array) != 1 and len(south_array) != 1:
        north_median = north_array[len(north_array) // 2]
        south_median = south_array[len(south_array) // 2]
        print(north_median)
        print(south_median)
        if north_median == south_median:
            result = north_median
            break
        elif north_median > south_median:
            north_array = north_array[:len(north_array) // 2]
            south_array = south_array[len(south_array) // 2:]
        else:
            north_array = north_array[len(north_array) // 2:]
            south_array = south_array[:len(south_array) // 2]
        print(north_array)
        print(south_array)
    print(f'result is = {north_median}')
    # ALGORITHM: compare medians of these arrays first and then you should change direction of intervals
    # Then if we got that medians are equal we can that is the median for merged array of those two


if __name__ == '__main__':
    main()