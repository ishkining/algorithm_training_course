import sys


def find_order_parenthesis(letter, open_parenthesis=True):
    if open_parenthesis:
        return ['(', '{', '['].index(letter)
    else:
        return [')', '}', ']'].index(letter)


def main():
    our_line = [letter for letter in sys.stdin.readline().rstrip()]
    stack = []
    result = True
    for parenthesis_index in range(len(our_line)):
        if our_line[parenthesis_index] in ['(', '[', '{']:
            stack.append(find_order_parenthesis(our_line[parenthesis_index]))
        elif find_order_parenthesis(our_line[parenthesis_index], False) == stack[-1]:
            stack.pop()
        else:
            result = False
            break
    print(result)


if __name__ == '__main__':
    main()