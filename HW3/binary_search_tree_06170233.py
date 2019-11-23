class TreeNode: 
    def __init__(self,x): 
        self.left = None
        self.right = None
        self.val = x

class Solution(object):
    


    def insert(self,root,val): 
        if root is None: 
            root = TreeNode(val) 
        else: 
            if val > root.val: 
                if root.right is None: 
                    root.right = TreeNode(val)
                    return root.right
                else: 
                    return self.insert(root.right, val) 
                    
            else: 
                if root.left is None: 
                    root.left = TreeNode(val)
                    return root.left
                else: 
                    return self.insert(root.left,val) 

        return TreeNode(val)
    def search(self, root, target):
        if root.val==target : 
            return root
        if root is None :
            return None
  

        if root.val >= target: 
            return self.search(root.left,target)
    
        else:
            return self.search(root.right,target)
        
        
        
    
    def findleftnode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_target(self, root, target):
        if root is None:
            return None
        else:
            if root.val == target:
                return root
            elif root.val < target:
                return self.find_target(root.right, target)
            else:
                return self.find_target(root.left, target)

    def delete(self, root, target):
        while self.find_target(root, target) is not None:
            if root is None:
                return root
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif target > root.val:
                root.right = self.delete(root.right, target)
            else:
                if root.right is None and root.left is not None:
                    x = root.left
                    root = None
                    return x
                elif root.left is None and root.right is not None:
                    x = root.right
                    root = None
                    return x

                x = self.findleftnode(root.right)
                root.val = x.val
                root.right = self.delete(root.right, x.val)
        return root
    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else: 
            k=0                                          
            a=self.search(root,target)
            while a != None and a.val == target:
                k=k+1
                a=a.left
                self.delete(root,target)
            while k>0:
                self.insert(root,new_val)
                k=k-1
            return root 
