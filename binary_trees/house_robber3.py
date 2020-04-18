class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rob(root):
    def dfs(node):
        if not node:
            return 0, 0

        left = dfs(node.left)
        right = dfs(node.right)
        max_upto_here_with_current_node = node.val + \
            left[1] + right[1]
        max_upto_here_without_current_node = max(
            left[0], left[1]) + max(right[0], right[1])
        return (max_upto_here_with_current_node, max_upto_here_without_current_node)
    return max(dfs(root))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(rob(root))
