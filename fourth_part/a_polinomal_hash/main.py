def main():
    number_a = int(input())
    number_m = int(input())
    line_s = input()
    result_hash = 0
    for index in range(len(line_s)):
        result_hash += ord(line_s[-1 * index - 1]) * number_a ** index
    result_hash %= number_m
    print(result_hash)


if __name__ == '__main__':
    main()