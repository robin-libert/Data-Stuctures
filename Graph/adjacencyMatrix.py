# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:52:06 2017

@author: USER
"""

class Vertex:

    def __init__(self, n):
        self.name = n
        self.id = 0
    
    def set_id(self, num):
        self.id = num
        
class Graph:
    
    def __init__(self):
        self.edges = []
        self.id = 0;
        
    def add_vertex(self, vertex):
        vertex.set_id(self.id)
        self.id += 1
        self.edges.append([])
        for i in self.edges:
            i.append(0)
        for e in range(len(self.edges)-1):
            self.edges[len(self.edges)-1].append(0)
    
    def add_edge(self, vertex1, vertex2):
        self.edges[vertex1.id][vertex2.id] = 1
            
    def print_graph(self):
        for e in self.edges:
            for i in e:
                print(i, end = " ")
            print("")
        
def exemple_utilisation():
        g = Graph()
        s1 = Vertex("1")
        s2 = Vertex("2")
        s3 = Vertex("3")
        s4 = Vertex("4")
        
        g.add_vertex(s1)
        g.add_vertex(s2)
        g.add_vertex(s3)
        g.add_vertex(s4)
        g.add_edge(s1, s2)
        g.add_edge(s2, s3)
        g.add_edge(s1, s3)
        g.add_edge(s3, s4)
        g.print_graph()
  
if __name__ == '__main__':         
    exemple_utilisation()
                
        