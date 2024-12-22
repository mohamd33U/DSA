# Recursive Python program to find length
# or count of nodes in a linked list

# Linked List Node
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Recursively count number of nodes in linked list
def count_nodes(head):
    # Base Case
    if head is None:
        return 0

    # Count this node plus the rest of the list
    return 1 + count_nodes(head.next)


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