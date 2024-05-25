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

    def inorder(self,root,result):
        if root is not None:
            self.inorder(root.left,result)
            result.append(root.data)
            self.inorder(root.right,result)
        print(result)
'''
class traverse(trees):
    def inorder(self, root, result):
        if root is not None:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)
        print(result)

    def postorder(self, root, result):
        if root is not None:
            result.append(root.data)
            self.postorder(root.left, result)
            self.postorder(root.right, result)
        print(result)

    def preorder(self, root, result):
        if root is not None:
            self.preorder(root.left, result)
            self.preorder(root.right, result)
            result.append(root.data)
        print(result)
'''



#Driver Code
tree=trees()
root=tree.createNode(5)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

tree.inorder(root,result=[])






