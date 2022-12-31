def get_parenthesis(open, close, line=''):
    if open == 0 and close == 0:
        print(line)
    elif open == close and open >= 1:
        get_parenthesis(open - 1, close, line + '(')
    else:
        if open >= 1:
            get_parenthesis(open - 1, close, line + '(')
        if close - 1 >= open and close >= 1:
            get_parenthesis(open, close - 1, line + ')')


def main():
    number = int(input())
    get_parenthesis(number, number)


if __name__ == '__main__':
    main()
