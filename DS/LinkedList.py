class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # TO PRINT PRINT LINKED LIST (TRAVERSE)
    def print_list(self):
        temp = self.head
        result = []
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        print(result)
    
    # TO ADD ITEM AT THE END (TAIL)
    def push(self,value)->bool:
        new_node = Node(value)
        if self.length == 0:
            self.head=  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # TO REMOVE ITEM FROM THE END (TAIL)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while (temp.next):
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    # TO ADD ITEM AT THE START (HEAD)
    def unshift(self,value)->bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # TO REMOVE ITEM FROM THE START (HEAD)
    def shift(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
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
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # TO INSERT NEW NODE AT GIVEN INDEX
    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.unshift(value)
        if index == self.length - 1:
            return self.push(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # TO REMOVE NODE AT GIVEN INDEX
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        
    
    # TO REVERSE THE LINKED LIST
    def reverse(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        
            
            
            
            
            
linked_list = LinkedList(5)
linked_list.push(6)
linked_list.push(8)
linked_list.unshift(2)
linked_list.unshift(3)
linked_list.print_list()
linked_list.insert(2,7)
print(linked_list.get(1).value)
linked_list.print_list()
linked_list.remove(2)
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()