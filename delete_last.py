def remove_last_node(self):
    if self.head is None:
        return
    curr=self.head
    while(curr and curr.next.next):
        curr=curr.next

    curr.next=None