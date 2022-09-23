class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.prev = None
        self.next = None
    

class DoublyLinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # TO PRINT DOUBLY LINKED LIST
    def print_list(self):
        temp = self.head
        result = []
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        print(result)
        
    # TO ADD ITEM AT THE END (TAIL)
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # TO REMOVE ITEM AT THE END (TAIL)
    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    # TO ADD ITEM AT THE START (HEAD)
    def unshift(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    # TO REMOVE ITEM FROM THE START (HEAD)
    def shift(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
        
    # TO GET ITEM BY INDEX
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # TO SET VALUE AT GIVEN INDEX
    def set(self,index,value):
        temp = self.get(index-1)
        if temp:
            temp.value = value
            return True
        return False
    
    # TO INSERT ITEM AT GIVEN INDEX
    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.unshift(value)
        elif index == self.length -1:
            return self.push(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
            
    
    # TO REMOVE ITEM FROM GIVEN INDEX
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = prev.next
            prev.next = temp.next
            temp.next.prev = prev
            temp.prev = None
            temp.next = None
            self.length -= 1
            return temp
    
    
    
    
dbl = DoublyLinkedList(5)
dbl.push(3)
dbl.push(7)
dbl.push(9)
dbl.print_list()
dbl.pop()
dbl.pop()
dbl.print_list()
dbl.push(11)
dbl.shift()
print(dbl.get(1).value)
dbl.print_list()
dbl.insert(1,55)
dbl.insert(1,45)
dbl.print_list()
dbl.remove(2)
dbl.print_list()