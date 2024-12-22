#[Expected Approach] Using Two Pointers – One Pass – O(M) Time and O(1) Space

# Python3 program to find Nth node from end of linked list

# Link list node
class Node:
  
      # Constructor to initialize a new node with data
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to find Nth node from the end of linked list
def nth_from_end(head, N):

    # Create two pointers main_ptr and ref_ptr 
    # initially pointing to head.
    main_ptr = head
    ref_ptr = head

    # Move ref_ptr to the N-th node from beginning.
    for _ in range(1, N):
        ref_ptr = ref_ptr.next

        # If the ref_ptr reaches None, then it means
        # N > length of linked list
        if ref_ptr is None:
            return -1

    # Move ref_ptr and main_ptr by one node until
    # ref_ptr reaches last node of the list.
    while ref_ptr.next is not None:
        ref_ptr = ref_ptr.next
        main_ptr = main_ptr.next

    return main_ptr.data

if __name__ == "__main__":
      
    # Create a hard-coded linked list:
    # 35 -> 15 -> 4 -> 20
    head = Node(35)
    head.next = Node(15)
    head.next.next = Node(4)
    head.next.next.next = Node(20)

    # Function Call to find the 4th node from end
    print(nth_from_end(head, 4))
