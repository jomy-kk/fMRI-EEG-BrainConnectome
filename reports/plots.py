import matplotlib.pyplot as plt

def plot_adjacency_matrix(matrix, intensity_name, plot_name, show=False):
    plt.imshow(matrix, cmap='jet', interpolation='nearest')
    cbar = plt.colorbar()
    cbar.set_label(intensity_name)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/" + plot_name + ".pdf",
        format='pdf', pad_inches=0, dpi=1200)
    if show: plt.show()
