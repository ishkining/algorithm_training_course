# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:

        def get_path(root):
            left_side, right_side = [], []
            if root.left:
                for piece in get_path(root.left):
                    left_side.append(str(root.val) + str(piece))
            if root.right:
                for piece in get_path(root.right):
                    right_side.append(str(root.val) + str(piece))
            if not root.right and not root.left:
                return str(root.val)

            return left_side + right_side

        return sum(int(number) for number in get_path(root))