class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zig_zag(node):
    nodes_level_wise = []
    nodes_in_level = [node]

    while node and nodes_in_level:
        nodes_value = []
        next_level = []

        for node in nodes_in_level:
            nodes_value.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        nodes_level_wise.append(nodes_value)
        nodes_in_level = next_level

    return invert_helper(nodes_level_wise)


def invert_helper(nodes_level_wise):
    for i in range(len(nodes_level_wise)):
        if i % 2 != 0:
            temp = nodes_level_wise[i]
            nodes_level_wise[i] = temp[::-1]

    return nodes_level_wise


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(zig_zag(root))
