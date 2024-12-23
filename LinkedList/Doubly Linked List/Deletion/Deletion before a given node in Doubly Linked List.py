# Python Program to delete a node before a
# given node of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def delete_before(head, key):
    curr = head

    # Find the node with the given key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr is None or curr.prev is None,
    # there is no node to delete
    if curr is None or curr.prev is None:
        return head

    # Node to be deleted
    nodeToDelete = curr.prev

    # Update the prev of the current node to the prev
    # of the node to be deleted
    curr.prev = nodeToDelete.prev

    # If nodeToDelete's prev is not None, update its
    # next pointer to the current node
    if nodeToDelete.prev is not None:
        nodeToDelete.prev.next = curr
    else:
        # If nodeToDelete is the head node
        head = curr

    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()


if __name__ == "__main__":
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    head = delete_before(head, 3)
    print_list(head)