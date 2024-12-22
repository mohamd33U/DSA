#[Naive Approach] By Finding the length of list – Two Pass – O(M) Time and O(1) Space


# Python3 program to find Nth node from end of linked list

# Link list node
class Node:
  
   # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to find the Nth node from the last of a linked list
def findNthFromLast(head, N):
    length = 0
    temp = head

    # Count the number of nodes in Linked List
    while temp is not None:
        temp = temp.next
        length += 1

    # Check if value of N is not more than length of the linked list
    if length < N:
        return -1

    temp = head

    # Get the (length - N + 1)th node from the beginning
    for _ in range(1, length - N + 1):
        temp = temp.next

    return temp.data

if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 35 -> 15 -> 4 -> 20
    head = Node(35)
    head.next = Node(15)
    head.next.next = Node(4)
    head.next.next.next = Node(20)

    # Function Call to find the 4th node from end
    print(findNthFromLast(head, 4))