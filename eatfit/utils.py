import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 8))
    plt.title('Média do feedback dado pelos utilizadores de 1 (Pouca) a 5 (Muita)')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Critério')
    plt.ylabel('Avaliação')
    plt.tight_layout
    graph = get_graph()
    return graph


def get_pie(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 8))
    plt.title('Respostas ao Quiz')
    sizes = [x,y]
    labels = 'Certas','Erradas'
    explode = (0.1,0)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.tight_layout
    graph = get_graph()
    return graph
