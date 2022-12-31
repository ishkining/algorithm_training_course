import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip().split(' ')
    k_num = int(input())
    counter_dict = {}
    for number in line:
        counter_dict[number] = counter_dict.get(number, 0) + 1

    counter_dict = {k : v for k, v in sorted(counter_dict.items(), key=lambda counter: counter[1], reverse=True)}
    result = ''
    counter = 0
    for k, _ in counter_dict.items():
        if counter == k_num:
            break
        result += k + ' '
        counter += 1
    print(result)


if __name__ == '__main__':
    main()