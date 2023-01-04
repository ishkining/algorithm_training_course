class Solution(object):
    def isSameTree(self, p, q):
        return self.get_Tree(p) == self.get_Tree(q)

    def get_Tree(self, tree):
        result = []
        stack = [tree]
        while stack != []:
            node = stack.pop(0)
            if node:
                result.append(node.val)
                if node.left or node.right:
                    stack.append(node.left)
                    stack.append(node.right)
            else:
                result.append(None)
        return result