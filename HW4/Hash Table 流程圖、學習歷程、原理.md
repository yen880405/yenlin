**流程圖**




<img src='https://github.com/yen880405/yenlin/blob/master/image/hashtable.jpg' height=500 weight =500>





**學習歷程**

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```


* 首先我先設計一個空的linkedlist

```python
def __init__(self):
        """
        Initialize your data structure here.
        """
		# the size of your hashset is self-defined
        self.size = 1000
        self.arr = [None for _ in range(self.size)]
```

* 依leetcode題目規則設立以上初始值


```python
 def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.size
        if not self.arr[idx]:
            return
        head = self.arr[idx]
        while head:
            if head.val == key:
                return True
            head = head.next
        return False
```


* 後來嘗試利用原理餘數概念加入linkedlist中，而其中contain是要最先完成的function


```python
    def add(self, key: int) -> None:
        idx = key%self.size
        if not self.arr[idx]:
            self.arr[idx] = ListNode(key)
        else:
            head = self.arr[idx]
            while head.val != key and head.next:
                head = head.next
            if head.val != key:
                head.next = ListNode(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        idx = key % self.size
        if self.arr[idx].val == key:
            self.arr[idx] = self.arr[idx].next
            return
        head = self.arr[idx]
        while head.next.val != key:
            head = head.next
        head.next = head.next.next
```

* 最後利用linkedlist的概念去設計完add和remove

**這些都是上星期二演算法課時老師利用pair programing時達成的大部分進度，個人覺得我因為此形式的互動，獲得很多這次作業的養分，與夥伴沒有太多熟識，也因此沒有浪費太多時間在無意義的打屁閒聊，對作業的進度有一大進展，也很有幫助**

* 之後幾天再加上MD5編碼及加上助教格式，其中capacity一開始最讓我疑惑，不太懂那個變數名稱是什麼意思，後來睡前想一想突然想到這就是hash table的精髓啊，利用餘數放入規定空間數量內，最後整理加上MD5及改對的格式，原本有想說MD5要用一個新的def來創建之後再呼叫，但我遇到了些瓶頸不知道如何突破，所以最後決定在每個裡面都加上MD5的編碼，也因此成功跑出測資。

 
