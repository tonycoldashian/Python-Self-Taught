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

    def Insert_At_End(self,data):
        newnode = Node(data)
        ptr = self.head

        if ptr is None:
            head = newnode

        else:
            while (ptr is not None):
                ptr = ptr.ref
                
            ptr = newnode



#limkedlist 
LL1 = LinkedList()
LL1.Insert_At_End(100)
LL1.Insert_At_End(10)
LL1.Insert_At_End(20)
LL1.Insert_At_End(30)
LL1.print_LL()