import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,number,x):
        self.number = number
        self.x = x
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None


    # def insert(self, number, node, x):
    #     if node == None:
    #         new_node = Node(number,x)
    #         return new_node
    #     else:
    #         if x > node.x:
    #             node.right = self._insert(node.right,number,x)
    #         else:
    #             node.left = self._insert(node.left,number,x)
    #     return node


    def insert(self,number,x):
        self.root = self._insert(self.root,number,x)#4,3

    def _insert(self,node,number,x):
        if node == None:
            new_node = Node(number,x)
            return new_node
        else:#self.root의 해드 :(node(7,8)), node의 right = None, left= None
            #파라미터로 넘어온 number, x = 4,3
            if x > node.x:# 3, 8
                node.right = self._insert(node.right,number,x)
            else:# none, 4,3
                node.left = self._insert(node.left,number,x)
        return node
    
    def preorder(self):
        lis = []
        def _preorder(node):
            lis.append(node.number)
            if node.left != None: _preorder(node.left)
            if node.right != None: _preorder(node.right) 
        _preorder(self.root)
        return lis

    def postorder(self):
        lis = []
        def _postorder(node):
            if node.left != None: _postorder(node.left)
            if node.right != None: _postorder(node.right)
            lis.append(node.number) 
        _postorder(self.root)
        return lis

def solution(nodeinfo):
    idx = [i for i in range(1,len(nodeinfo)+1)]
    nodeinfo = list(zip(idx,nodeinfo))
    nodeinfo.sort(key = lambda x : x[1][1], reverse = True)
    
    tree = Tree()
    for i,l in nodeinfo:
        tree.insert(i,l[0])
    pr = tree.preorder()
    po = tree.postorder()
    return [pr,po]
    
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))