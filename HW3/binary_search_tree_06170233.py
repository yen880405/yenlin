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
        
        
        
    
    def minValueNode(node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target < root.val:
                root.left = self.delete(root.left, target)

            elif target > root.val:
                root.right = self.delete(root.right, target)

            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp

                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = self.minValueNode(root.right)

                root.val = temp.val
            
                root.right = self.delete(root.right, temp.val)

            return root
    def modify(self, root, target, new_val):
        if root is None: 
            root = TreeNode(new_val) 
        else: 
            if new_val > root.val: 
                if root.right is None: 
                    root.right = TreeNode(new_val)
                    return root.right
                else: 
                    return self.insert(root.right, new_val) 
                    
            else: 
                if root.left is None: 
                    root.left = TreeNode(new_val)
                    return root.left
                else: 
                    return self.insert(root.left,new_val) 
            return True
