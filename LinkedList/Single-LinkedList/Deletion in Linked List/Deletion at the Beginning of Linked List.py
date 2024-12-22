# Python program to delete a node from the beginning of given
# linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Function to delete the head node


def delete_head(head):
  
    # Base case if linked list is empty
    if head is None:
        return None

    # Change the head pointer to the next node
    # and free the original head
    temp = head
    head = head.next

    # Free the original head
    del temp

    # Return the new head
    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    # Creating a linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_list(head)
    # Deleting the head node
    head = delete_head(head)
    print("List after deleting the head: ")
    print_list(head)