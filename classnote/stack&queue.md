# stack邏輯圖解
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.06.26.png'>
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.06.38.png'>
# queue邏輯圖解
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.06.47.png'>
<img src='https://github.com/yen880405/yenlin/blob/master/classnote/image/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-07%20%E4%B8%8B%E5%8D%8810.06.53.png'>

# stack python code
```python
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
```
# stack python code
```python
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
```

參考資料：https://stackabuse.com/stacks-and-queues-in-python/
