import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title("Graph Example")
nodes = []
edges = []
data = [('Джеймс Мэй', 'Джереми Кларксон'),
 ('Ричард Хаммонд', 'Джереми Кларксон'),
 ('Антон Савенков', 'Джереми Кларксон', 'Топ Гир'),
 ('Ричард Хаммонд', 'Джеймс Мэй'),
 ('Антон Савенков', 'Джеймс Мэй', 'Топ Гир'),
 ('Антон Савенков', 'Ричард Хаммонд', 'Топ Гир')]

for row in data:
    nodes.append(Node(id=row[0], label=row[0], size=400))
    nodes.append(Node(id=row[1], size=400) )
    edges.append(Edge(source=row[0], target=row[1]))
config = Config(width=1000, 
                height=1000, 
                directed=False,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)