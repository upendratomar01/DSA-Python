class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    

class Queue:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    # TO PRINT PRINT QUEUE (TRAVERSE)
    def print_queue(self):
        temp = self.first
        result = []
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        print(result)
    
    # TO ADD ITEM TO QUEUE (END)
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    # TO REMOVE ITEM FROM QUEUE (START)
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return temp
    
    
    
    
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(8)
queue.enqueue(18)
queue.print_queue()
queue.dequeue()
queue.dequeue()
queue.print_queue()