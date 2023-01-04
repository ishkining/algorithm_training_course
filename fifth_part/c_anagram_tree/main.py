class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    root = Node(1, node5, node6)

    def get_side(root, reversed=False):
        stack = [root]
        values = []
        while stack:
            node = stack.pop(0)
            values.append(node.val)
            if reversed:
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

        return values
    print(get_side(root.left, False))
    print(get_side(root.right, True))
    print(get_side(root.left, False) == get_side(root.right, True))


if __name__ == '__main__':
    main()