import sys
import math


def main():
    line = sys.stdin.readline().rstrip()
    calculation_array = line.split()
    stack = []
    while len(calculation_array) > 0:
        operand = calculation_array.pop(0)
        if 48 <= ord(operand[-1]) <= 57:
            stack.append(int(operand))
        else:
            first_element = stack.pop()
            second_element = stack.pop()
            if operand == '+':
                stack.append(first_element + second_element)
            elif operand == '-':
                stack.append(second_element - first_element)
            elif operand == '/':
                stack.append(math.floor(second_element / first_element))
            elif operand == '*':
                stack.append(second_element * first_element)
    print(stack[-1])


if __name__ == '__main__':
    main()