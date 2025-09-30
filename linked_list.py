class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=1
    
    def insert(self,value,index):
        current=self.head

        for i in range(index):
            current=current.next
            
        new_node=Node(value)
        next_node=current.next
        current.next=new_node
        new_node.next=next_node
        self.length+=1
    
    def delete(self,index):
        current=self.head

        for i in range(index):
            before=current
            current=current.next

        before.next=current.next
        self.length-=1
        
    def all_print(self):
        print(f"Linked list length : {self.length}")
        current=self.head
        for i in range(self.length):
            print(current.value,end=" | ")
            current=current.next