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

*最後利用linkedlist的概念去設計完add和remove
