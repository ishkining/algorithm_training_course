class Node:
    def __init__(self, value, next_item = None):
        self.value = value
        self.next_item = next_item


def solution(node: Node, elem):
    counter = 0
    while node:
        if node.value == elem:
            return counter
        node = node.next_item
        counter += 1
    return -1


def main():
    first_node = Node('hey im here')
    second_node = Node('second shit here', first_node)
    third_node = Node('how u do baby', second_node)
    fourth_node = Node('no one deserved it', third_node)

    print(solution(fourth_node, 'how u do baby'))


if __name__ == '__main__':
    main()
