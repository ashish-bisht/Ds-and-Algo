# DFS inorder , iterative


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(node):
    path = []
    stack = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            temp_node = stack.pop()
            path.append(temp_node.val)
            node = temp_node.right
    return path


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(inorder_traversal(root))
