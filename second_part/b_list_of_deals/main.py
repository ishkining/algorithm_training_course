class Node:
    def __init__(self, value, next_item = None):
        self.value = value
        self.next_item = next_item


def solution(node):
    while node:
        print(node.value)
        node = node.next_item


def main():
    first_deal = Node('run stream', None)
    second_deal = Node('imitate to solve tasks', first_deal)
    third_deal = Node('lie about push ups', second_deal)
    fourth_deal = Node('wake up', third_deal)

    solution(fourth_deal)


if __name__ == '__main__':
    main()