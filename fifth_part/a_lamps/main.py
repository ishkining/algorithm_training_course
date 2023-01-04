class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def main():
    left_sub_1 = Node(2)
    left_sub_2 = Node(7)
    left_header = Node(3, left_sub_1, left_sub_2)
    right_sub_1 = Node(4)
    right_sub_2 = Node(8)
    right_header = Node(5, right_sub_1, right_sub_2)
    header_node = Node(1, left_header, right_header)

    #   task Time
    stack = [header_node]
    values = []
    while stack:
        node = stack.pop(0)
        values.append(node.value)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)

    print(max(values))


if __name__ == '__main__':
    main()
