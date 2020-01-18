class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def max_path_sum(self, node):
        self.max_sum = float('-inf')
        self.dfs(node)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        left_sum = max(0, self.dfs(node.left))
        right_sum = max(0, self.dfs(node.right))

        self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)

        return max(left_sum, right_sum) + node.val


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(5)


sol = Solution()


print(sol.max_path_sum(root))
