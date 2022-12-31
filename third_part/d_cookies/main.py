import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    kids_array = [int(number) for number in line.split(' ')]
    m = int(input())
    line = sys.stdin.readline().rstrip()
    cookie_array = [int(number) for number in line.split(' ')]
    kids_array.sort()
    cookie_array.sort()
    counter_feed_kids = 0
    for cookie in cookie_array:
        if cookie >= kids_array[counter_feed_kids]:
            counter_feed_kids += 1
            if counter_feed_kids == len(kids_array):
                break
    print(counter_feed_kids)


if __name__ == '__main__':
    main()