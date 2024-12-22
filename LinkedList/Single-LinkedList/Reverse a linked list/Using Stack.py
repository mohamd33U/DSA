#[Alternate Approach – 2] Using Stack – O(n) Time and O(n) Space

# Python program to reverse linked list using Stack

class Node:
    def __init__(self, new_data):
          
        self.data = new_data
        self.next = None

def reverse_list(head):
      
    # Create a stack to store the nodes
    stack = []
  
    temp = head
  
    # Push all nodes except the last node into stack
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
  
    # Make the last node as new head of the linked list
    head = temp
  
    # Pop all the nodes and append to the linked list
    while stack:
          
        # append the top value of stack in list
        temp.next = stack.pop()
        
        # move to the next node in the list
        temp = temp.next
  
    # Update the next pointer of last node 
    # of stack to None
    temp.next = None
  
    return head

def print_list(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()


# Create a hard-coded linked list:
# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given Linked List:", end="")
print_list(head)

head = reverse_list(head)

print("Reversed Linked List:", end="")
print_list(head)