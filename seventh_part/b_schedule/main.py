import sys


def main():
    n = int(input())
    list_times = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip().split()
        list_times.append((float(line[1]) - float(line[0]), float(line[0]), float(line[1])))
    list_times = list(sorted(list_times, key=lambda element: element))
    print(list_times)
    result = [list_times.pop(0)]
    for index in range(len(list_times)):
        if result[-1][2] <= list_times[index][1] or result[-1][1] >= list_times[index][2]:
            result.append(list_times[index])
    print(len(result))
    [print(str(el[1]) + ' ' + str(el[2])) for el in result]


if __name__ == '__main__':
    main()