import io
import base64
import pandas as pd
from flask import Flask
from wtforms import Form, validators, SelectField
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

with app.open_resource('static/data.csv') as f:
    df = pd.read_csv(f)  # reading csv from pandas

with app.open_resource('static/drop_down.csv') as p:
    drop_down = pd.read_csv(p) 

positions = drop_down.iloc[:, 0].tolist()

class InputForm(Form):
    A = SelectField(
        label='Start Position', choices = positions)
    B = SelectField(
        label='End Position', choices = positions)


G = nx.Graph()  # initializing a graph

#making list of the columns in the data file
job_position = df.iloc[:, 0].tolist()
promoted_from_1 = df.iloc[:, 1].tolist()
promoted_from_2 = df.iloc[:, 2].tolist()
promoted_from_3 = df.iloc[:, 3].tolist()
promoted_to_1 = df.iloc[:, 4].tolist()
promoted_to_2 = df.iloc[:, 5].tolist()
promoted_to_3 = df.iloc[:, 6].tolist()

for i in range(len(job_position)):  # adding the edges to the graph with lists
    G.add_edge(job_position[i], promoted_from_1[i])

for i in range(len(job_position)):
    G.add_edge(job_position[i], promoted_from_2[i])

for i in range(len(job_position)):
    G.add_edge(job_position[i], promoted_from_3[i])

for i in range(len(job_position)):
    G.add_edge(job_position[i], promoted_to_1[i])

for i in range(len(job_position)):
    G.add_edge(job_position[i], promoted_to_2[i])

for i in range(len(job_position)):
    G.add_edge(job_position[i], promoted_to_3[i])

def mapp(start,end):
    img = io.BytesIO()
    p = nx.shortest_path(G,start,end)  # finding the shortest path

    # Set color of edges of the map to grey
    for e in G.edges():
        G[e[0]][e[1]]['color'] = '#e2e2e2'
    # Set color of path of the map to red
    for i in range(len(p) - 1):
        G[p[i]][p[i + 1]]['color'] = '#a30000'
    

    edge_color_list = [G[e[0]][e[1]]['color'] for e in G.edges()]

    #canvas size
    plt.figure(figsize=(30, 30))
    #drawing the map on the canvas
    nx.draw_networkx(G, edge_color=edge_color_list, 
                        with_labels=True, 
                        font_size=7, 
                        node_color='#ade2ff', 
                        node_size=1000)
    plt.axis('off')
    #saving the image as a png
    plt.savefig(img, format='png')
    img.seek(0)
    img = base64.b64encode(img.getvalue()).decode()
    #displaying image
    return img


