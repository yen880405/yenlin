
# coding: utf-8

# In[3]:



from collections import defaultdict 

class Graph:
     
    def __init__(self): 
         self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    
    
    def BFS(self, s):
        state2 = []
        queue = [s]

        while queue:
            s = queue.pop(0)
            
            if s not in state2:
                state2.append(s)
                neighbours = self.graph[s]
                
                for neighbour in neighbours:
                    queue.append(neighbour)
        return state2

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

