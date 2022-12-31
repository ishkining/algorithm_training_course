combination_array = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                     ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
result_combinations = ''


def get_combinations(numbers: str, result=''):
    global result_combinations
    if len(numbers) == 0:
        result_combinations += result + ' '
    else:
        first_char = int(numbers[0]) - 2
        for character in combination_array[first_char]:
            get_combinations(numbers[1:], result + character)


def main():
    our_input_numbers = input()
    get_combinations(our_input_numbers)
    print(result_combinations[:-1])


if __name__ == '__main__':
    main()
