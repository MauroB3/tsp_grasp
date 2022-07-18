import matplotlib.pyplot as plt


def plot_result(x, x_label, y, y_label, nombre):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.xticks(fontsize=8)
    ax = plt.subplot()
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    plt.ylabel(y_label)
    plt.title(nombre)
    ruta = './images/' + nombre + '.jpg'
    plt.savefig(ruta)
    plt.show()


def write_result(camino, costo, nombre):
    nombre_archivo = './resultados/resultado_' + nombre + '.txt'
    with open(nombre_archivo, 'w') as file:
        file.write("Resultado para " + nombre + '\n')
        file.write("Camino hamiltoniano: " + str(camino) + '\n')
        file.write("Valor: " + str(costo))
        file.close()
