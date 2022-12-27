class Node:
    def __init__(self, value, next_item = None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    stack = []
    counter = 0
    while node:
        if counter != idx:
            stack.append(node.value)
        node = node.next_item
        counter += 1

    result_node = None
    while stack:
        result_node = Node(stack.pop(0), result_node)

    return result_node


def main():
    first_node = Node('I wanna open this card')
    second_node = Node('I lost my mind hel me', first_node)
    third_node = Node('I sit on chair', second_node)
    fourth_node = Node('I lie with you', third_node)

    solution(fourth_node, 2)


if __name__ == '__main__':
    main()