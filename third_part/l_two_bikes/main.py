import sys


def get_day(array: list, price: int) -> int:
    start, end = 0, len(array)
    while start < end:
        mid = (start + end) // 2
        if array[mid - 1] < price <= array[mid]:
            return mid + 1
        elif array[mid] > price:
            end = mid
        else:
            start = mid
    return -1


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    input_array = [int(number) for number in line.split(' ')]
    bike_price = int(input())
    print(get_day(input_array, bike_price))
    print(get_day(input_array, 2*bike_price))


if __name__ == '__main__':
    main()