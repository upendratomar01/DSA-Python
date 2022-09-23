class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    

class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    # TO PRINT PRINT STACK (TRAVERSE)
    def print_stack(self):
        temp = self.top
        result = []
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        print(result)
        
    # TO ADD ITEM INTO THE STACK (PUSH)
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
            
        
    # TO REMOVE ITEM FROM THE STACK (POP)
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp
    
    
    
stack = Stack(5)
stack.push(1)
stack.push(3)
stack.push(8)
stack.push(18)
stack.print_stack()
stack.pop()
stack.pop()
stack.print_stack()

        