class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_binary_tree(root):
    if root is None:
        return

    swap(root)

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)


def swap(root):
    root.left, root.right = root.right, root.left


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(7)
    root.left.left.left = Node(8)
    root.leftleft.right = Node(9)
