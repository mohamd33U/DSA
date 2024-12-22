#Search an element in a Linked List (Recursive Approach) – O(N) Time and O(N) Space:



# Recursive Python program to search
# an element in linked list

# A Linked List Node
class Node:
  
      # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Checks whether the key is present in linked list
def searchKey(head, key):
  
    # Base case
    if head is None:
        return False

    # If key is present in current node, return true
    if head.data == key:
        return True

    # Recur for remaining list
    return searchKey(head.next, key)

# Driver code
if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 14 -> 21 -> 13 -> 30 -> 10
    head = Node(14)
    head.next = Node(21)
    head.next.next = Node(13)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(10)

    # Key to search in the linked list
    key = 14

    if searchKey(head, key):
        print("Yes")
    else:
        print("No")