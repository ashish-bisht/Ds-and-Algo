class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def closest_value_in_bst(node, target):
    return closest_helper(node, target, float("inf"))


def closest_helper(node, target, closest):
    if node is None:
        return closest
    if abs(closest - target) > abs(node.val - target):
        closest = node.val

    if target >= node.val:
        return closest_helper(node.right, target, closest)

    elif target < node.val:
        return closest_helper(node.left, target, closest)

    else:
        return closest


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

    print(closest_value_in_bst(root, 12))
