 def preorder(root):
     if root is None:
         return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
    
    
def treeHeight(root):
       if  root is None:
           return -1
        left_height=treeHeight(root.left)
        right_height=treeHeight(root.right):
        return 1+max(left_height,right_height)
         
         
treeHeight(1)     waiting
treeHeight(2)    waiting
.
.
.
treeHeight(None)

BST                     AvgTime     Worst-case Time
Search                    O(logn)                 O(n)
Insert
Delete

def search(root,key):
    if root is  None  or root.val==key:
        return root
    if key<root.val:
        return search(root.left,key)
    return search(root.right, key)

class TreeNode:
    def __init__(self, key):
        ...
        ...
        ...
#OR:      
def searchBST(root,val):
    while root is not None:
        if root.val==val:
            return root
        elif val<root.val:
            root=root.left
        else:
            root=root.right
     return None        # iterative space / space complexity   O(1)
 #space complexity 
 #  skewed tree( n )-recursive space?    O(n) 
 #  balanced tree    -recursive space     O(logn)

 def insert(root,key):
     if root is None:
         return TreeNode(key)
    if key<root.key:
        root.left=insert(root.left,key)
    elif key>root.key:
        root.right=insert(root.right,key)
    return root
        
root=None
for i in[8,3,10,16,6]:
    root=insert(root,i)


 def delete(root,key):
     if root is None:
         return None
     if key<root.val:
         root.left=delete(root.left,key)
     elif key>root.val:
         root.right=delete(root.right,key)
      else:
          # case 1: no children
          if root.left is None and root.right is None:
              return None
          # case 2: has 1 child
          if root.left is None:
              return root.right
          if root.right is None:
                return root.left
            # case 3: has 2 children
             successor=root.right
             while successor.left is not None:
                 successor=successor.left
             root.val=successor.val
             root.right=delete(root.right, successor.val)
         return root
