
class doubly:

    class nodes():
         __slots__=('element','previous','next')
         
         def __init__(self,element,previous,next):
            self.element=element
            self.previous=previous
            self.next=next
    #SENTINALS 
    def __init__(self):
        self.head=self.nodes(None,None,None)
        self.tail=self.nodes(None,None,None)
        self.head.next=self.tail
        self.tail.previous=self.head
        self.size=0

    def len(self):
        return self.size
    
    def empty(self):
        return self.size==0
    
    def insertbet(self,ele,predecessor,successor):
        newest=self.nodes(ele,predecessor,successor)
        predecessor.next=newest
        successor.previous=newest
        self.size+=1
        return newest
    
    def delnode(self,nodes):
        predecessor=nodes.previous
        successor=nodes.next
        predecessor.next=successor
        successor.previous=predecessor
        self.size-=1
        element=nodes.element
        nodes.previous=nodes.next=nodes.element=None

        return element
    
    def prt(self):
        temp=self.head.next
        while(temp!=self.tail):
            print(temp.element,end=' ')
            temp=temp.next

    def add(self,list1):
        temp=self.tail.previous
        #while (temp!= self.tail):
        #    temp =temp.next

        current=list1.head.next

        while (current != list1.tail):
            new=self.nodes(current.element,temp,self.tail)
            temp.next=new
            self.tail.previous=new
            temp=new
            current=current.next
        list1=None
        



my_doubly_linked_list = doubly()
node1=my_doubly_linked_list.head
noden=my_doubly_linked_list.tail
node2=my_doubly_linked_list.insertbet(5,node1,noden)
node3=my_doubly_linked_list.insertbet(7,node2,noden)
node4=my_doubly_linked_list.insertbet(8,node3,noden)
node7=my_doubly_linked_list.insertbet(4,node4,noden)
node8=my_doubly_linked_list.insertbet(2,node7,noden)


my_doubly_linked_list2 = doubly()
node1=my_doubly_linked_list2.head
noden=my_doubly_linked_list2.tail
node2=my_doubly_linked_list2.insertbet(2,node1,noden)
node3=my_doubly_linked_list2.insertbet(8,node2,noden)
node4=my_doubly_linked_list2.insertbet(3,node3,noden)
node7=my_doubly_linked_list2.insertbet(5,node4,noden)
node8=my_doubly_linked_list2.insertbet(9,node7,noden)


my_doubly_linked_list.add(my_doubly_linked_list2)


my_doubly_linked_list.prt()

