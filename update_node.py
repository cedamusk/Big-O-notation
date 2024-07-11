def updateNode(self,val,index):
    current_node=self.head
    position=0
    if position==index:
        current_node.data=val
    else:
        while(current_node != None and position != index):
            position=position+1
            current_node=current_node.next

        if current_node !=None:
            current_node.data=val
        else:
            print("Index not present")



def updateNode(self, val, index):
  if index < 0 or index >= len(self.data):
    raise IndexError("Index out of bounds")
  self.data[index] = val

