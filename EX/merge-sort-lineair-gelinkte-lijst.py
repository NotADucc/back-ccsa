

class Node:

    def __init__(self, data=None, next_node=None):
        """ data     : de gegevens die je wil opslaan in deze `Node`.
            next_node: de volgende `Node` in de lineair gelinkte lijst.
        """
        self.data = data
        self.next = next_node

def print_list(head):
    items = []

    ### BEGIN JOUW CODE
    while head is not None :
        items.append(head.data)
        head = head.next
    ### EINDE JOUW CODE

    print("[" + ",".join(str(_) for _ in items) + "]")

def merge(head_1, head_2):      
    head = Node()
    curr = head
    while head_1 is not None and head_2 is not None :
        if head_1.data < head_2.data :
            temp = head_1.next
            head_1.next = None
            curr.next = head_1
            head_1 = temp
        else :
            temp = head_2.next
            head_2.next = None
            curr.next = head_2
            head_2 = temp
        curr = curr.next
        
    while head_1 is not None :
        temp = head_1.next
        head_1.next = None
        curr.next = head_1
        head_1 = temp
        curr = curr.next
        
    while head_2 is not None :
        temp = head_2.next
        head_2.next = None
        curr.next = head_2
        head_2 = temp
        curr = curr.next
        
    return head.next

def split(head):
    first = head
    second = head
    fast = head
    
    while fast is not None and fast.next is not None :
        if fast.next.next is not None :
            first = first.next
        second = second.next
        fast = fast.next.next
        
    if fast is not None :
        second = second.next 

    first.next = None
    
    return (head, second)
def merge_sort(head):
    if head is None or head.next is None :
        return head
    h1, h2 = split(head)
    h1 = merge_sort(h1)
    h2 = merge_sort(h2)
    return merge(h1, h2)