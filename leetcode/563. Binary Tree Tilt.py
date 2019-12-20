class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.left_vals = []
        if root.left:
            self.getValues(root.left,self.left_vals)
        self.right_vals = []
        if root.right:
            self.getValues(root.right,self.right_vals)
        return abs(sum(self.left_vals)-sum(self.right_vals)) + self.findTilt(root.left) + self.findTilt(root.right)
        
    def getValues(self,root,vals):
        if not root:
            return
        vals.append(root.val)
        if root.left:
            self.getValues(root.left,vals)
        if root.right:
            self.getValues(root.right,vals)
