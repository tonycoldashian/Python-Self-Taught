class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head == None:
            print("Empty")
        else:
            ptr = self.head
            while(ptr is not None):
                print(ptr.data)
                ptr = ptr.ref

    def Insert_At_Start(self,data):
        newnode = Node(data)
        newnode.ref = self.head
        self.head = newnode

    def Insert_end(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        
        else:
            ptr = self.head
            while ptr.ref is not None:
                ptr = ptr.ref
            
            ptr.ref = newnode

    def delete_begin(self):
        self.head = self.head.ref



#limkedlist 
LL1 = LinkedList()
LL1.Insert_end(100)
LL1.Insert_end(10)
LL1.Insert_end(20)
LL1.Insert_end(30)

LL1.print_LL() 
print("\n")

LL1.delete_begin()

LL1.print_LL()