import sys


def main():
    line_s = sys.stdin.readline().rstrip()
    line_t = sys.stdin.readline().rstrip()
    dict_chars_s, dict_chars_t = {}, {}
    is_it_comparable = True
    for index in range(len(line_s)):
        if dict_chars_t.get(line_t[index], None) or dict_chars_s.get(line_s[index], None):
            if dict_chars_t.get(line_t[index], None) != line_s[index] \
                    or dict_chars_s.get(line_s[index], None) != line_t[index]:
                is_it_comparable = False
        else:
            dict_chars_t[line_t[index]] = line_s[index]
            dict_chars_s[line_s[index]] = line_t[index]

    if is_it_comparable:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()