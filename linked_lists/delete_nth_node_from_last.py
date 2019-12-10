class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_nth_node(head, n):
    if not head:
        return

    first = head
    second = head

    count = 1
    while count <= n:
        second = second.next
        count += 1

    if second is None:
        return head.next

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next


def display(head):
    while head:
        print(head.val, "-->", end=" ")
        head = head.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print(display(head))

    remove_nth_node(head, 3)

    print(display(head))
