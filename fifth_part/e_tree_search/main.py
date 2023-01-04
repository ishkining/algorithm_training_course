class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def node_comparison(root) -> (bool, int, int):
    if not root:
        return True, None, None

    node_st_l, min_l, max_l = node_comparison(root.left)
    node_st_r, min_r, max_r = node_comparison(root.right)

    node_st = node_st_l and node_st_r and (not max_l or max_l < root.val) and (not min_r or root.val < min_r)
    min_value = min([number for number in [min_l, min_r, root.val] if number])
    max_value = max([number for number in [max_l, max_r, root.val] if number])
    return node_st, min_value, max_value


def main():
    root1 = Node(1, None, None)
    root2 = Node(4, None, None)
    root3 = Node(3, root1, root2)
    root4 = Node(8, None, None)
    root5 = Node(5, root3, root4)

    print(node_comparison(root5)[0])


if __name__ == '__main__':
    main()


