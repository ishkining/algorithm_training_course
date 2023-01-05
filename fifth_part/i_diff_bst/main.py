def get_fibb(number: int) -> int:
    if number == 0:
        return 1
    return get_fibb(number - 1) * number


input_n = 3
result = int((get_fibb(2 * input_n)) / (get_fibb(input_n) * get_fibb(input_n + 1)))
print(result)