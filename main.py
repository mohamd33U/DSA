class Node:
    def __init__(self,data):
        self.data=data
        self.prev =None
        self.next=None

def print_list(head):
    curr=head
    while curr:
        print(f"{curr.data}",end='<->')
        curr=curr.next
    print("None")
def insert_at_front(head, data):
    new_node=Node(data)
    new_node.next=head
    head.prev=new_node


if __name__ == "__main__":
    # Create a hardcoded doubly linked list:
    # 2 <-> 3 <-> 4
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end='')
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Node at the front:", end='')
    data = 1
    head = insert_at_front(head, data)

    # Print the updated list
    print_list(head)