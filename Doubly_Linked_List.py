#This doubly Linked List class allows for forward and backward traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,new_value):
        self.value = new_value

    def setNext(self,new_next):
        self.next = new_next

    def getPrevious(self):
        return self.prev

    def setPrevious(self,new_prev):
        self.prev = new_prev

    def __str__(self):
        return ("{}".format(self.value)) 

    __repr__ = __str__
                        
 

class DoublyLinkedList:
    #DoublyLinkedList() creates a new doubly linked list that is empty. It needs no parameters and returns nothings. Items must be unique. 
    def __init__(self):
        self.head = None
  
    def addFirst(self, value):
        #adds a new Node with value= item at the beginning of the list. It needs the item and returns nothing.
        new_node= Node(value)
        if self.head== None:
            self.head= new_node
        else:
            self.head.prev= new_node
            new_node.next= self.head
            self.head= new_node        

        
    def addLast(self, value):
        #adds a new Node with value= item at the end of the list. It needs the item and returns nothing.
        new_node= Node(value)
        temp= self.head
        while temp.next!= None:
            temp= temp.next
        temp.next= new_node
        new_node.prev= temp
 
    def addBefore(self, pnode_value, value):
        #adds a new Node with value= item before the Node with value= pnode_value. It needs the value of reference Node and the item to be added and returns nothing. Assume the reference node is already in the list.
        new_node= Node(value)
        temp= self.head
        while temp.value!= pnode_value:
            pre= temp
            temp= temp.next
        if temp.prev== None:
            new_node.next= temp
            temp.prev= new_node
            self.head= new_node
        else:
            pre.next= new_node
            new_node.prev= pre
            new_node.next= temp
            temp.prev= new_node
 
    def addAfter(self, pnode_value, value):
        #adds a new Node with value= item after the Node with value= pnode_value. It needs the value of reference Node and the item to be added and returns nothing. Assume the reference node is already in the list.
        new_node= Node(value)
        temp= self.head
        while temp.value!= pnode_value:
            temp= temp.next
        if temp.next==None:
            temp.next= new_node
            new_node.prev= temp
        else:
            temp.next.prev= new_node
            new_node.next= temp.next
            temp.next= new_node
            new_node.prev= temp

    def printDLL(self):
        temp=self.head
        print("\nTraversal Head to Tail")
        while temp:
            print(temp.getValue(), end=' ')
            last = temp
            temp=temp.getNext()
 
        print("\nTraversal Tail to Head")
        while(last is not None):
            print(last.getValue(), end=' ')
            last = last.prev

    def getNode(self,value):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getValue()==value:
                found=True
                return current
            else:
                current=current.getNext()
        return

#Test cases
'''
dll=DoublyLinkedList()
dll.addFirst(5)
dll.addFirst(9)
dll.addFirst(4)
dll.addFirst(3)
print(dll.head)
dll.addLast(8)
dll.addLast(12)
dll.addLast(56)
dll.printDLL()
dll.addBefore(56, 44)
dll.addBefore(9,32)
dll.addAfter(56,756)
dll.addAfter(8,47)
dll.printDLL()
dll.addLast(999)
dll.addFirst(856)
print('')
print(dll.head)
dll.printDLL()
'''