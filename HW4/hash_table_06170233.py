from Crypto.Hash import MD5


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    
    def add(self, key) :
        h = MD5.new()
        h.update(key.encode("utf-8"))
        num = int(h.hexdigest(),16)
        idx = num % self.capacity
        if not self.data[idx]:
            self.data[idx] = ListNode(num)
        else:
            head = self.data[idx]
            while head.val != num and head.next:
                head = head.next
            if head.val != num:
                head.next = ListNode(num)

    def remove(self, key) :
        h = MD5.new()
        h.update(key.encode("utf-8"))
        num = int(h.hexdigest(),16)
        
        if not self.contains(key):
            return 
        idx = num % self.capacity
        if self.data[idx].val == num:
            self.data[idx] = self.data[idx].next
            return 
        head = self.data[idx]
        while head.next.val != num:
            head = head.next
        head.next = head.next.next

    def contains(self, key) :
        
        h = MD5.new()
        h.update(key.encode("utf-8"))
        num = int(h.hexdigest(),16)
        
        idx = num % self.capacity
        if not self.data[idx]:
            return False
        head = self.data[idx]
        while head:
            if head.val == num:
                return True
            head = head.next
        return False
