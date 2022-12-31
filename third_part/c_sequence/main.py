def is_it_sequence(s, t):
    if len(s) == 0:
        return True
    else:
        char_index = t.index(s[0])
        if char_index == -1:
            return False
        return is_it_sequence(s[1:], t[char_index:])


def main():
    s_sequence = input()
    t_sequence = input()
    print(is_it_sequence(s_sequence, t_sequence))


if __name__ == '__main__':
    main()
