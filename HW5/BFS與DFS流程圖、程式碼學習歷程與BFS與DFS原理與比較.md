**BFS與DFS原理與比較**

*BFS*

* 定義

BFS (Breadth-First-Search) ——廣度優先搜尋, 是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置， 無論如何都要遍歷完畢整張地圖才終止。 按照就近原則進行， 距離原點相同的節點的訪問順序是相近的。


BFS將數字照順序擺放上去，利用QUEUE序列，把adjacency的數字照排上state1(queue)，
後再放下state2輸出;而DFS將state1變成stack形式，因為需要使用最上層也就是最後一個數字，所以需要使用stack這個平常用來undo的功能。
此外，bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。
反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體。


**BFS與DFS流程圖**




<img src='https://github.com/yen880405/yenlin/blob/master/image/BFS%E8%88%87DFS.jpg' height=500 weight =500>


**學習歷程＊＊




```python
 def __init__(self): 
    self.graph = defaultdict(list) 
 
 def addEdge(self,u,v): 
    self.graph[u].append(v)
```

參考完網路上作品開始上工
這兩段是不用添加任何東西的，在設定初始init跟addedge


```python
 def BFS(self, s):
        state2 = []
        queue  = [s]

        while queue:
            s = queue.pop(0)
            
            if s not in state2:
                state2.append(s)
                neighbours = self.graph[s]
                
                for neighbour in neighbours:
                    queue.append(neighbour)
        return state2
```

先設定一個state2及一個bfs重要因子queue序列空間，原本忘記pop這個用法，上網搜尋了一下重拾記憶，順便連append也一同搞懂，照著流程圖真的很快擁有邏輯，再一步一步換成程式碼，雖然每次都在這花了許多時間，但應該是有慢慢在進步當中！


```python
 def DFS(self, s): 
        stateb = []
        stack = [s]

        while stack:
            s = stack.pop(-1)
            if s not in stateb:
                stateb.append(s)
                neighbours = self.graph[s]
                for neighbour in neighbours:
                    stack.append(neighbour)
        return stateb
```

這段跟bfs大同小異，畢竟這兩樣幾乎同個概念，只差在queue變stack跟pop的順序，而原因在流程圖即比較那邊有較詳盡的說明，在這就先不做贅述。
主要這次程式碼能完成，要感謝在pair programing時，彥南在旁釐清觀念，要我不要急，才能按部就班完成想法構思，
也感謝蔡老師上課教學的改變，使我流程圖及邏輯更能掌握，不再那麼抽象，特別是bfs跟dfs寫在黑板的例題，需要寫很多東西，謝謝不厭其煩，讓我懂更快速。


**參考資料**

https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search/46383689

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
