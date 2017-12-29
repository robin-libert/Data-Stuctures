# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:52:06 2017

@author: USER
"""

import random as random


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
        
    def add_edge_distance(self, vertex1, vertex2, distance):
        self.edges[vertex1.id][vertex2.id] = distance
    """
    Cette fonction permet de générer un graphe automatiquement.
    number_v est le nombre de sommets désiré.
    max_distances est la distance maximale qu'il peut y avaoir entre 2 sommets.
    """    
    def generator(self, number_v, max_distances, densite):
        list_vertices = []
        #On crée des sommets et on les ajoute à la liste de sommets
        for i in range(number_v):
            v = Vertex(str(i))
            self.add_vertex(v)
            list_vertices.append(v)
        #On va lier des sommets ensemble en fonction de la densité du graphe
        for j in range(int(densite*(len(list_vertices)*(len(list_vertices)-1)))):
            index = 0
            index2 = 0
            #On vérifie que les index ne soient pas les mêmes pour évité qu'un sommet est une distance >0 pour s'atteindre lui même.
            while index == index2:
                index = random.randint(0,number_v-1)
                index2 = random.randint(0,number_v-1)
            #Si 2 sommets ne sont pas encore lié on les lie ensemble de manière non orienté
            if self.edges[list_vertices[index].id][list_vertices[index2].id] == 0 and self.edges[list_vertices[index2].id][list_vertices[index].id] == 0:
                dist = random.randint(1, max_distances)
                self.add_edge_distance(list_vertices[index], list_vertices[index2],dist)
                self.add_edge_distance(list_vertices[index2], list_vertices[index], dist)
            
    def print_graph(self):
        for e in self.edges:
            for i in e:
                print(i, end = " ")
            print("")
        
def exemple1():
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

def exemple2():
    g = Graph()
    g.generator(5, 10,0.8)
    g.print_graph()
  
if __name__ == '__main__':         
    exemple2()
        