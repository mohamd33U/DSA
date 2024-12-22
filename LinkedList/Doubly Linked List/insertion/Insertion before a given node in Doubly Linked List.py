# Python Program to insert a node before a given node of
# doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Function to insert a new node before a given node
# in doubly linked list
def insert_before(head, key, new_data):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr becomes None, the given key is not found in the linked list
    if curr is None:
        return head

    # Create a new node
    new_node = Node(new_data)

    # Set prev of new node to prev of given node
    new_node.prev = curr.prev

    # Set next of new node to given node
    new_node.next = curr

    # Update next of given node's prev to new node
    if curr.prev is not None:
        curr.prev.next = new_node
    else:
        # If the current node is the head, update the head
        head = new_node

    # Update prev of given node to new node
    curr.prev = new_node

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Create a hardcoded doubly linked list:
    # 1 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node before node with data 3
    print("Inserting Node with data 2 before node 3:", end="")
    data = 2
    key = 3
    head = insert_before(head, key, data)

    # Print the updated list
    print_list(head)