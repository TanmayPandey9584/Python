class MinHeap():
    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return (i-1)//2

    def leftchild(self,i):
        return 2*i+1

    def rightchild(self,i):
        return 2*i+2

    def heapify(self,i):
        left=self.leftchild(i)
        right=self.rightchild(i)
        smallest=i
        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right

        if smallest!=i:
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            self.heapify(smallest)

    def delete_min(self):
        root=self.heap[0]
        if len(self.heap)==0:
            return
        if len(self.heap)==1:
            return self.heap.pop()

        self.heap[0]=self.heap.pop()
        self.heapify(0)
        return root

    def insert(self,key):
        self.heap.append(key)
        i=len(self.heap)-1

        while i!=0 and self.heap[self.parent(i)]>self.heap[i]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)

    def build_heap(self,array):
        self.heap=array
        for i in range(len(self.heap//2)-1,-1,-1):
            self.heapify(i)

    def printheap(self):
        print("\n")
        print("Min Heap")
        for i in range(len(self.heap)):
            print(self.heap[i])


if __name__=="__main__":
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(2)
    heap.insert(6);heap.insert(4)
    heap.insert(5)
    heap.insert(7)
    print(heap.delete_min())  # Output: 1
    print(heap.delete_min())  # Output: 2
    print(heap.delete_min())

    heap.printheap()




