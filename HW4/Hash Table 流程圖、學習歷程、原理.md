**流程圖**




<img src='https://github.com/yen880405/yenlin/blob/master/image/hashtable.jpg' height=500 weight =500>





**Hash Table原理**

* Hash Table:也可稱作 HashMap，Hash Table 是儲存 (key, value) 這種 mapping 關係的一種資料結構，從上圖中可以很清楚地看到是 Dictionary 類別中雜湊表的一種實作。實作的思路大概是，當要把資料放到雜湊表時，先給定一個 key 和存放的 value，並將 key 的每個字元轉換成 ASCII Code 或 Unicode Code 並相加，這個相加的值即是 hash 鍵值，在 table 陣列上對應到存放的 value。

* Hash Function:Hash Table 好不好用的關鍵跟這個神奇的 hash function 有很大的關係。讓我們想像一種情況，如果我們使用一個壞掉的 hash function，不管餵給這個 hash function 什麼內容他都會吐出同一個 index，那這樣的話就跟存一個 array 沒什麼兩樣。 搜尋的時間複雜度就會變成 O(n)。
以實用的角度出發，在簡單認識 Hash Table 的時候並不需要理解 hash function 要怎麼實作，但是我們要知道，hash function沒有完美的，有可能會把兩個不同的 key 指到同一個桶子，這就是所謂的 collision。當 collision 發生的時候，除了最直觀地增加 Hash Table 的桶子數，在每個桶子中用一個 linked list 來儲存 value、或是 linear probe 都是常用的方法，不過我們就先不細究下去。


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

**REFERENCE：**

http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/

https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/

https://leetcode.com/problems/design-hashset/

還有pair programing的夥伴，但我不知道她叫什麼名字
