class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_lst(node):
    final = dummy = Node(0)
    dummy.next = node

    while dummy and dummy.next and dummy.next.next:
        p1 = dummy.next
        p2 = p1.next

        dummy.next = p2
        p1.next = p2.next
        p2.next = p1

        dummy = p1

    return final.next


def display_linked_list(node):
    while node:
        print(node.val)
        node = node.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


print(display_linked_list(reverse_linked_lst(head)))
