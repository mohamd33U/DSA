# Python program to delete the last node of linked list

# Node structure for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to remove the last node of the linked list
def remove_last_node(head):
    # If the list is empty, return None
    if not head:
        return None

    # If the list has only one node, delete it and return None
    if not head.next:
        return None

    # Find the second last node
    second_last = head
    while second_last.next.next:
        second_last = second_last.next

    # Delete the last node
    second_last.next = None

    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_list(head)

    # Removing the last node
    head = remove_last_node(head)

    print("List after removing the last node: ")
    print_list(head)