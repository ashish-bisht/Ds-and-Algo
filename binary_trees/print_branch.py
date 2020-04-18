class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_paths(node):
    traverse(node, [])


def traverse(node, path):
    if not node:
        return

    path.append(node.val)

    if node.left is None and node.right is None:
        print(path)

    traverse(node.left, path)
    traverse(node.right, path)
    path.pop()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(tree_paths(root))
