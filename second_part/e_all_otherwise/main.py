class DoubleConnectedNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode):
    stack = []
    while node:
        stack.append(node.value)
        node = node.next

    result_node = None
    while len(stack) > 0:
        result_node = DoubleConnectedNode(stack.pop(), None, result_node)

    return result_node


def main():
    third_node = DoubleConnectedNode('i')
    second_node = DoubleConnectedNode('u', third_node)
    first_node = DoubleConnectedNode('h', second_node)

    solution(first_node)


if __name__ == '__main__':
    main()