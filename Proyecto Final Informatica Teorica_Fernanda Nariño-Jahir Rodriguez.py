#Declaracion de la librerias a utilizar
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#se define la clase Graphapp
class GraphApp:
    def __init__(G, master):
        G.master = master
        G.master.title("Dijkstra Shortest Path Visualization")

        # sentencia que Crea un grafo de ejemplo
        G.graph = nx.Graph()
        node_names = ["Anton", "Cabuya", "El chiru", "El retiro", "El valle", "Juan diaz", "Rio hato", "San juan de dios", "Santa rita", "Caballero",
                      "Penonome", "Cañaveral","Cocle", "Chiguiri arriba", "El coco", "Pajonal", "Rio grande", "Rio indio", "Toabre", "Tulu","Aguadulce",
                      "El cristo", "El roble", "pocri", "Barrios unidos", "Pueblos unidos", "Virgen del carmen", "El hato",
                      "La pintada", "El harino", "El Potrero", "Llano Grande", "Piedras Gordas", "Las Lomas", "Llano Norte",
                      "Ola", "El Cope", "El Palmar", "El Picacho", "La Pava","Nata de los caballeros", "Capellania", "El Caño", "Guzman", "Las Huacas","Toza","Villarreal"]
        G.graph.add_nodes_from(node_names)
        #sentencia que permite agregar el peso de las aristas a los nodos
        G.graph.add_edges_from([("Anton", "Penonome", {"weight": 15.6}),
                                   ("Cabuya", "Caballero", {"weight": 3.3}),
                                   ("El chiru", "Anton", {"weight": 6.4}),
                                   ("El retiro", "Santa rita", {"weight": 3.9}),
                                   ("El valle", "Caballero", {"weight": 10.1}),
                                   ("Juan diaz", "Penonome", {"weight": 2.0}),
                                   ("Rio hato", "El chiru", {"weight": 12.9}),
                                   ("Rio hato", "El valle", {"weight": 12.9}),
                                   ("San juan de dios", "Juan diaz", {"weight": 3.9}),
                                   ("Santa rita", "Juan diaz", {"weight": 11.6}),
                                   ("Caballero", "Juan diaz", {"weight": 13.4}),
                                   ####Corregimientos de Penonome#########
                                   ("Penonome", "Rio grande", {"weight":15.0 }),
                                   ("Cañaveral", "Penonome", {"weight": 8.7}),
                                   ("Cocle", "Rio grande", {"weight": 5}),
                                   ("Cocle", "Penonome", {"weight": 13.4}),
                                   ("Chiguiri arriba", "Pajonal", {"weight":11.4 }),
                                   ("El coco", "Penonome", {"weight":14.3 }),
                                   ("Pajonal", "Penonome", {"weight": 13.9}),
                                   ("Rio grande", "Aguadulce", {"weight":22.3 }),
                                   ("Rio indio", "Chiguiri arriba", {"weight": 13.0}),
                                   ("Toabre", "Pajonal", {"weight":9.4 }),
                                   ("Tulu", "Toabre", {"weight":14.9}),
                                   #####Corregimientos de Aguadulce#########
                                   ("Aguadulce", "pocri", {"weight": 1.9}),
                                   ("El cristo", "pocri", {"weight": 10.5}),
                                   ("Barrios unidos", "Aguadulce", {"weight": 6.4}),
                                   ("Pueblos unidos", "El roble", {"weight": 5.0}),
                                   ("Virgen del carmen", "pocri", {"weight": 1.2}),
                                   ("El hato", "El cristo", {"weight": 2.3}),
                                   ("Aguadulce", "El roble", {"weight": 14.6}),
                                    #####Corregimientos de La Pintada#########
                                   ("La pintada", "Cañaveral", {"weight":8.4 }),
                                   ("El harino", "Piedras Gordas", {"weight": 4.4}),
                                   ("El Potrero", "La pintada", {"weight": 11.5}),
                                   ("Llano Grande", "La pintada", {"weight":4.4 }),
                                   ("Piedras Gordas", "La pintada", {"weight":8.9}),
                                   ("Piedras Gordas", "Las Lomas", {"weight":11.8}),
                                   ("Llano Norte", "Llano Grande", {"weight": 16.4}),
                                    #####Corregimientos de Olá#########
                                   ("Ola", "Rio grande", {"weight":19.0 }),
                                   ("El Cope", "Ola", {"weight": 3.6 }),
                                   ("El Palmar", "El Cope", {"weight":15.4 }),
                                   ("El Picacho", "Ola", {"weight":2.6}),
                                   ("La Pava", "Ola", {"weight":4.7}),
                                    #####Corregimientos de Nata#########
                                   ("Nata de los caballeros", "Rio grande", {"weight":12.8}),
                                   ("Nata de los caballeros", "Aguadulce", {"weight":9.3}),
                                   ("Capellania", "Nata de los caballeros", {"weight":5.7}),
                                   ("El Caño", "Rio grande", {"weight": 6.7}),
                                   ("Guzman", "El Caño", {"weight": 9.0}),
                                   ("Las Huacas", "Ola", {"weight": 12.5}),
                                   ("Las Huacas", "Toza", {"weight": 17.9}),
                                   ("Toza","Capellania", {"weight": 10.7}),
                                   ("Villarreal", "Capellania", {"weight": 10.3}),
                                   ("Villarreal", "Toza", {"weight": 2.9})]),

        G.positions = nx.spring_layout(G.graph)
        G.path_edges = []

        # permite crear Variables de control para los menús desplegables
        G.start_node_var = tk.StringVar()
        G.end_node_var = tk.StringVar()

        # permite inicializar la interfaz gráfica
        G.init_gui()

    def init_gui(G):
        # Crear ventana para el grafo
        graph_window = tk.Toplevel(G.master)
        graph_window.title("Graph Window")
        
        # Crear un lienzo para el grafo
        G.fig, G.ax = plt.subplots()
        G.ax.set_facecolor('Wheat') # permite dar color al lienzo
        G.canvas = FigureCanvasTkAgg(G.fig, master=graph_window)
        G.canvas_widget = G.canvas.get_tk_widget()
        G.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Permite crear la ventana principal para la interfaz gráfica
        main_window = G.master
        # Permite cambiar el color de fondo a menta
        G.master.configure(bg="Darkgray") 

        # Crear menús desplegables para seleccionar nodos de inicio y fin
        start_label = ttk.Label(main_window, text="¿Donde te encuentras?")
        start_label.pack(pady=5)
        start_menu = ttk.Combobox(main_window, textvariable=G.start_node_var,
                                  values=list(G.graph.nodes))
        start_menu.pack(pady=5)

        end_label = ttk.Label(main_window, text="¿A Donde Quieres ir?")
        end_label.pack(pady=5)
        end_menu = ttk.Combobox(main_window, textvariable=G.end_node_var,
                                values=list(G.graph.nodes))
        end_menu.pack(pady=5)

        # Botón para encontrar la ruta más corta
        find_button = ttk.Button(main_window, text="Encontrar Ruta",
                                 command=G.find_shortest_path)
        find_button.pack(pady=10)

    def find_shortest_path(G):
        start_node = G.start_node_var.get()
        end_node = G.end_node_var.get()

        # Ejecucion del algoritmo de Dijkstra
        shortest_path = nx.shortest_path(G.graph, source=start_node, target=end_node, weight="weight")
        G.path_edges = list(zip(shortest_path, shortest_path[1:]))

        # Dibujar el grafo
        G.draw_graph()
        
    
    def draw_graph(G):
        # Limpiar la visualización anterior
        G.ax.clear()

        # Dibuja los nodos y aristas
        nx.draw_networkx_nodes(G.graph, G.positions, node_size=150, node_color="cyan", ax=G.ax)
        nx.draw_networkx_edges(G.graph, G.positions, ax=G.ax)
        nx.draw_networkx_labels(G.graph, G.positions, font_size=9, ax=G.ax)

        # permite dibujar nodos de inicio y destino en colores específicos
        start_node = G.start_node_var.get()
        end_node = G.end_node_var.get()
        nx.draw_networkx_nodes(G.graph, G.positions, nodelist=[start_node], node_color="red", ax=G.ax)
        nx.draw_networkx_nodes(G.graph, G.positions, nodelist=[end_node], node_color="green", ax=G.ax)

        # Resalta la ruta más corta en rojo
        nx.draw_networkx_edges(G.graph, G.positions, edgelist=G.path_edges, edge_color="red", width=2, ax=G.ax)

        # Mostrar los pesos de las aristas
        edge_labels = nx.get_edge_attributes(G.graph, 'weight')
        nx.draw_networkx_edge_labels(G.graph, G.positions, edge_labels=edge_labels, ax=G.ax)

        # Calcular y muestra la distancia total recorrida
        total_distance = sum(G.graph.edges[edge]["weight"] for edge in G.path_edges)
        distance_text = f"Distancia total: {total_distance} km"
        G.ax.text(0.5, -0.1, distance_text, ha="center", va="center", transform=G.ax.transAxes)

        # Muestra los nodos visitados debajo de la distancia total
        shortest_path_nodes = nx.shortest_path(G.graph, source=start_node, target=end_node)
        visited_nodes_text = f"Nodos visitados: {' -> '.join(shortest_path_nodes)}"
        G.ax.text(0.5, -0.07, visited_nodes_text, ha="center", va="center", transform=G.ax.transAxes)

        # Actualiza la interfaz gráfica
        G.canvas.draw()    

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop() 