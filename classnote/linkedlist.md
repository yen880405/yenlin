# 簡介及特點

<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-08%20%E4%B8%8B%E5%8D%884.51.56.png'>
Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）。
因此，每個節點本身應該要有兩種屬性（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標（pointer）。
我想Linked-list與一般陣列（array）比起來最大的不同點在於：
陣列使用一連串的記憶體位置，因此可以透過array[index]直接存取資料，但是相對的，若要在陣列中加入或是刪除元素，則需要大量的資料搬移。
（python中的list雖然用法跟陣列很類似，並卻不是這樣子的實作方式，我在另一篇文章中有提到。而像是在C語言中，陣列所記錄的其實是第一個元素的地址，而index就是相對於第一個元素的偏移量了，所以才是從0開始。）
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-08%20%E4%B8%8B%E5%8D%884.52.01.png'>

而Linked-list的資料則散落在記憶體中各處，加入或是刪除元素只需要改變pointer即可完成，但是相對的，在資料的讀取上比較適合循序的使用，無法直接取得特定順序的值（比如說沒辦法直接知道list[3]）。

# 程式碼


```python
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.data, 
            temp = temp.next
  
  
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node 
  
    llist.printList()
```


參考資料：https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d
        https://www.geeksforgeeks.org/linked-list-set-1-introduction/
