def insertAtEnd(self,data):
    new_node=(data)
    if self.head is None:
        self.head=new_node
        return

    current_node=self.head
    while(current_node.next):
        current_node=current_node.next

    current_node.next=new_node