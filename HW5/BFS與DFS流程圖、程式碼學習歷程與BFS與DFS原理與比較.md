**BFS與DFS原理與比較**

BFS將數字照順序擺放上去，利用QUEUE序列，把adjacency的數字照排上state1(queue)，
後再放下state2輸出;而DFS將state1變成stack形式，因為需要使用最上層也就是最後一個數字，所以需要使用stack這個平常用來undo的功能。
此外，bfs會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。
反之，dfs是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以dfs更加省記憶體。


**BFS與DFS流程圖**




<img src='https://github.com/yen880405/yenlin/blob/master/image/BFS%E8%88%87DFS.jpg' height=500 weight =500>
