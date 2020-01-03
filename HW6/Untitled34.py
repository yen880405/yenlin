
# coding: utf-8

# In[32]:


from collections import defaultdict
import heapq
import math


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.weight = []
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                             for row in range(vertices)]

    # Dijkstra--------------------------------------------------------------------------------------------------
    def Dijkstra(self, s):
        s = str(s)
        graph_dict = self.get_graph_dict()
        if not graph_dict:
            return

        pri_queue = list()
        history = set()

        heapq.heappush(pri_queue, (0, s))

        combine = {s: None}
        distance = self.get_distance(graph_dict, s)

        while len(pri_queue) > 0:
            pair = heapq.heappop(pri_queue)
            span = pair[0]
            vertex = pair[1]
            history.add(vertex)

            path_list = graph_dict[vertex].keys()
            for path in path_list:
                if path not in history:
                    new_dist = span + graph_dict[vertex][path]
                    if new_dist < distance[path]:
                        heapq.heappush(pri_queue, (new_dist, path))
                        combine[path] = vertex
                        distance[path] = new_dist

        return distance

    def get_graph_dict(self) -> dict:
        if len(self.graph) == 0:
            return

        result = {}
        for point in range(len(self.graph)):
            path_list = self.graph[point]

            data = {}
            for other, span in enumerate(path_list):
                if other == point or span == 0:
                    continue
                data[str(other)] = span

            result[str(point)] = data

        return result

    def get_distance(self, graph_dict: dict, s: str):
        result = {s: 0}
        for vertex in graph_dict.keys():
            if vertex != s:
                result[vertex] = math.inf
        return result
    
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
        self.weight.append([u,v,w])
        self.weight=sorted(self.weight,key=lambda x:x[2])    
        
        
        
        
    def Kruskal(self):
        a=[]
        b={}
        for i in range(self.V):
            a.append(i)
        right=[]
        for vertix in self.weight:
            if a[vertix[1]] == a[vertix[0]] :
                pass
            else:
                right.append(vertix)
                for j in range(self.V):
                    if a[j]==a[vertix[1]]:
                        a[j]=a[vertix[0]]
                a[vertix[1]] ==a[vertix[0]]

        for k in right:
            name='{}-{}'.format(k[0],k[1])
            b[name]=k[2]                
        return b  
  

        

