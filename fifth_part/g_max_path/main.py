# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = -10 ** 9
        answer = self.get_path_sum(root)
        return self.max_path

    def get_path_sum(self, root):
        if not root:
            return 0
        left_side = max(self.get_path_sum(root.left), 0)
        right_side = max(self.get_path_sum(root.right), 0)
        if self.max_path < left_side + root.val + right_side:
            self.max_path = left_side + root.val + right_side
        return max(left_side, right_side) + root.val
