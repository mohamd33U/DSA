# Iterative Python program to count the number of nodes
# in a linked list


class Node:
    def __init__(self, new_data):

        # Constructor to initialize a new node with data
        self.data = new_data
        self.next = None


def count_nodes(head):

    # Counts number of nodes in linked list
    # Initialize count with 0
    count = 0

    # Initialize curr with head of Linked List
    curr = head

    # Traverse till we reach None
    while curr is not None:
        # Increment count by 1
        count += 1

        # Move pointer to next node
        curr = curr.next

    # Return the count of nodes
    return count


# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 1 -> 2 -> 1
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    # Function call to count the number of nodes
    print("Count of nodes is", count_nodes(head))