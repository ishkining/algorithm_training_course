def find_fibb(number):
    if number <= 1:
        return 1
    return find_fibb(number - 1) + find_fibb(number - 2)


def main():
    fibb_number = int(input())
    print(find_fibb(fibb_number))


if __name__ == '__main__':
    main()