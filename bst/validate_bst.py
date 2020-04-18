class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validate_bst(node):
    pass


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.left.left.left = Node(1)
    root.right.left = Node(13)
    root.right.right = Node(22)
    root.right.left.right = Node(14)

    print(validate_bst(root))
