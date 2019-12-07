class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def branch_sum(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, current_sum, sums):
    if node is None:
        return

    new_sum = current_sum + node.val
    if node.left is None and node.right is None:
        sums.append(new_sum)
        return

    calculate_branch_sums(node.left, new_sum, sums)
    calculate_branch_sums(node.right, new_sum, sums)


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.right = Node(10)
    root.right.left = Node(6)
    root.right.right = Node(7)

    def dfs(root, result):
        if not root:
            return
        dfs(root.left, result)
        result.append(root.val)
        dfs(root.right, result)
        return result

    print(dfs(root, []))

    print(branch_sum(root))
