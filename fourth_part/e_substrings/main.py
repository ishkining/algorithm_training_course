def main():
    our_input = input()

    typing_line = ''
    counter = 0
    max_counter = 0
    begin, end = 0, len(our_input)
    while begin < end:
        if our_input[begin] not in typing_line:
            typing_line += our_input[begin]
            counter += 1
        else:
            typing_line = typing_line[typing_line.index(our_input[begin]) + 1:] + our_input[begin]
            counter = len(typing_line)

        if counter > max_counter:
            max_counter = counter

        begin += 1

    print(max_counter)


if __name__ == '__main__':
    main()
