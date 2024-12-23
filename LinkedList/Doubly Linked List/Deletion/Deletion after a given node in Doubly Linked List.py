# Time Complexity: O(n),
# Auxiliary Space: O(1)
# Python Program to delete a node after a given
# node of doubly linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None


def delete_after(head, key):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr is None or curr.next is None,
    # there is no node to delete
    if curr is None or curr.next is None:
        return head

    # Node to be deleted
    node_delete = curr.next

    # Update the next of the current node to
    # the next of the node to be deleted
    curr.next = node_delete.next

    # If the node to be deleted is not the last node,
    # update the previous pointer of the next node
    if node_delete.next is not None:
        node_delete.next.prev = curr

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
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

    head = delete_after(head, 2)
    print_list(head)