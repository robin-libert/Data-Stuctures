# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:47:56 2017

@author: Robin
"""

"""
Cette classe représente un sommet.
"""
class Vertex:
    """
    Constructeur de la classe. Un sommet a un nom et une liste de voisins.
    """
    def __init__(self, n):
        self.name = n
        self.neighbors = []
      
    """
    Cette méthode permet d'ajouter un voisin v au sommet.
    """
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            
"""
Cette classe représente un graphe orienté sous forme de listes d'adjacences.
"""
class Graph:
    #Un graphe a une liste de sommets.
    def __init__(self):
        self.vertices = []
        
    """
    Cette méthode permet d'ajouter un sommet vertex au graphe.
    """
    def add_vertex(self, vertex):
        for e in self.vertices:
            if e == vertex:
                return False
        self.vertices.append(vertex)
        return True
    
    """
    Cette méthode permet de lier un sommet u à un sommet v à  l'aid ed'un arc orienté de u vers v.
    u et v seront des sommets voisins.
    """
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            u.add_neighbor(v)
            return True
        return False
    
    def print_graph(self):
        for e in self.vertices:
            print(e.name + " -> ", end = "")
            for i in e.neighbors:
                print(i.name + " ", end = "")
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
    