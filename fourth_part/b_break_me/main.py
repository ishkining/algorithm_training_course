from random import choice
from string import ascii_lowercase


def get_hash_code(line: str, a: int, m: int) -> int:
    result_hash = 0

    for index in range(len(line)):
        result_hash += ord(line[-1 * index - 1]) * a ** index

    return result_hash % m


def main():
    number_a = 1000
    number_m = 123987123
    is_isnt_over = True
    our_codes = {}
    while is_isnt_over:
        random_line = ''.join([choice(ascii_lowercase) for _ in range(18)])
        hash_code = get_hash_code(random_line, number_a, number_m)
        if our_codes.get(str(hash_code), None):
            is_isnt_over = False
            print(f'{hash_code} - {random_line}')
            print(f'{hash_code} - {our_codes[str(hash_code)]}')
        else:
            our_codes[str(hash_code)] = random_line


if __name__ == '__main__':
    main()