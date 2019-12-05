**流程圖**




<img src='https://github.com/yen880405/yenlin/blob/master/image/hashtable.jpg' height=500 weight =500>





**學習歷程**

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    # chain hash set
    def __init__(self,capacity):
        """
        Initialize your data structure here.
        """
        capacity=MD5.new()
        self.capacity=capacity
        self.data=[None]*capacity

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
