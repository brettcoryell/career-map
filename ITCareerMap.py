import pandas as pd #importing libraries
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#reading from a csv
df = pd.read_csv('/Users/akarshg/Desktop/OneDrive - NIU/OneDrive - Northern Illinois University/IT Career Map/IT_Career_Map.csv')

G=nx.Graph() #initializing a graph

#adding the nodes and edges
jp = [] #creating an empty array
for i in df.iloc[:,0]:
    jp.append(i) #adding column into an array

pf1 = []
for i in df.iloc[:,1]:
    pf1.append(i)

pf2 = []
for i in df.iloc[:,2]:
    pf2.append(i)

pf3 = []
for i in df.iloc[:,3]:
    pf3.append(i)

pt1 = []
for i in df.iloc[:,4]:
    pt1.append(i)

pt2 = []
for i in df.iloc[:,5]:
    pt2.append(i)

pt3 = []
for i in df.iloc[:,6]:
    pt3.append(i)

for i in range(len(jp)): #adding the edges
    G.add_edge(jp[i],pf1[i])

for i in range(len(jp)):
    G.add_edge(jp[i],pf2[i])

for i in range(len(jp)):
    G.add_edge(jp[i],pf3[i])

for i in range(len(jp)):
    G.add_edge(jp[i],pt1[i])

for i in range(len(jp)):
    G.add_edge(jp[i],pt2[i])

for i in range(len(jp)):
    G.add_edge(jp[i],pt3[i])

start_position = str(input("Enter start position: ")) #entering start_position
end_position = str(input("Enter end Position: "))#entering end_position
p = nx.shortest_path(G,start_position,end_position) #find the shortest path
print("The Shortest Path is",p) #displaying the shortest_path

for e in G.edges():
    G[e[0]][e[1]]['color'] = 'black'
# Set color of edges of the shortest path to blue
for i in range(len(p)-1):
    G[p[i]][p[i+1]]['color'] = 'blue'
# Store in a list to use for drawing
edge_color_list = [G[e[0]][e[1]]['color'] for e in G.edges()]
nx.draw_networkx(G, edge_color=edge_color_list, with_labels=True)
plt.show() #display's the graph
