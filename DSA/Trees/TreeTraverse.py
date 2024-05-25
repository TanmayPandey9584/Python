class trees:

    class Node():
        def __init__(self, value):
            self.left = None
            self.data = value
            self.right = None

    def createNode(self,data):
        return self.Node(data)

    def insert(self,node,data):
        if node is None:
            return self.createNode(data)

        if data<node.data:
            node.left=self.insert(node.left,data)

        else:
            node.right=self.insert(node.right,data)

        return node


    class traverse():
        def inorder(self, root, result):
            if root is not None:
                self.inorder(root.left, result)
                result.append(root.data)
                self.inorder(root.right, result)
            print(result)

        def postorder(self,root,result):
            if root is not None:
                result.append(root.data)
                self.postorder(root.left,result)
                self.postorder(root.right,result)
            print(result)

        def preorder(self,root,result):
            if root is not None:
                self.preorder(root.left,result)
                self.preorder(root.right,result)
                result.append(root.data)
            print(result)


root=trees()
root.traverse.inorder(root,result=[])
root.traverse.postorder(root,result=[])
root.traverse.preorder(root,result=[])