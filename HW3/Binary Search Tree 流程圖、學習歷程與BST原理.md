<img src='https://github.com/yen880405/yenlin/blob/master/image/bst2.jpg' height=500 weight =500>
新增的部分
<img src='https://github.com/yen880405/yenlin/blob/master/image/bst1.jpg' height=500 weight =500>
<img src='https://github.com/yen880405/yenlin/blob/master/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-11-22%20%E4%B8%8B%E5%8D%8812.13.39.png' height=500 weight =500>
原本中間程式碼都沒加return所以會出現上述的奇怪現象，而後加上了return就解決這個小問題。



```python



    def insert(self,root,val): 
        if root is None: 
            root = TreeNode(val) 
        else: 
            if val > root.val: 
                if root.right is None: 
                    root.right = TreeNode(val)
                    
                else: 
                    self.insert(root.right, val) 
                    
            else: 
                if root.left is None: 
                    root.left = TreeNode(val)
                    
                else: 
                    self.insert(root.left,val) 

        return TreeNode(val)
```
<img src='https://github.com/yen880405/yenlin/blob/master/image/bst.jpg' height=500 weight =500>
<img src='https://github.com/yen880405/yenlin/blob/master/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202019-11-22%20%E4%B8%8B%E5%8D%8812.40.33.png' height=500 weight =500>
search跟insert的錯誤差不多，還有一個問題是忘記加self在return後面，也因此卡了很長一段時間，
還有上述圖片問題，明明數字一樣卻出現False，後發現是因為兩個的類別不同的問題。





```python    
    def search(self, root, target):
        if root.val==target : 
            return root
        if root is None :
            return None
  

        if root.val >= target: 
            return self.search(root.left,target)
    
        else:
            return self.search(root.right,target)
```
        





```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print("insert")
print(Solution().insert(root1, 4) == root1.left.right)
print("------------------------------------------")
print(Solution().insert(root1, 4).val)
print(root1.left.right.val)
# search
print("search")
print(Solution().search(root2, 10) == root2.right.right)
print(Solution().search(root2, 10))
print(root2.right.right)
```

    insert
    True
    ------------------------------------------
    4
    4
    search
    True
    <__main__.TreeNode object at 0x10356d128>
    <__main__.TreeNode object at 0x10356d128>



<img src='https://github.com/yen880405/yenlin/blob/master/image/bst5.jpg' height=500 weight =500>

```python
 def delete(self, root, target):
        if root is None:
            return None

        if target < root.val:
            root.left =delete(root.left, target)

        elif target > root.val:
            root.right =delete(root.right, target)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = minValueNode(root.right)

            root.val = temp.val
            
            root.right = delete(root.right, temp.val)

        return root
```

原本打這樣卻一直有delete跟minvaluenode變數名稱為宣告的問題，爾後，加了self及以下宣告有改善


```python

class Solution(object):
    
    def minValueNode(node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, target):
        if root is None:
            return None

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



```

但後來又出先一個bug，其中一個測資會出現false，後來又改了while及一個等式，卡了兩個晚上，經詢問同學幫我找出這個問題，真的謝天謝地。



<img src='https://github.com/yen880405/yenlin/blob/master/image/bst6.jpg' height=500 weight =500>
```python


    def modify(self, root, target, new_val):
  
        right = root.right  
        rightMost = root  
  

        if (root.left): 

            rightMost = modifytree(root.left)  
            root.right = root.left  
            root.left = None

  
        if (not right): 
            return rightMost  
  

            rightMost.right = right  
  

            rightMost = modifytree(right)  
            return rightMost
```






modify到現在都還有問題只好先到這邊繳交作業了



參考資料：
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
