import matplotlib.pyplot as plt



def plot_connectivity_matrix(matrix, intensity_name, title, plot_name, show=False):
    plt.clf()
    plt.imshow(matrix, cmap='jet', interpolation='nearest')
    plt.title(title, fontsize=17)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    cbar = plt.colorbar()
    cbar.set_label(intensity_name)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/" + plot_name + ".pdf",
        format='pdf', pad_inches=0,  bbox_inches='tight', dpi=1200)
    if show: plt.show()


def plot_connectivity_matrix_thresholded(matrix, intensity_name, title, plot_name, show=False):
    plt.clf()
    plt.imshow(matrix, cmap='hot_r', interpolation='nearest')
    plt.title(title, fontsize=17)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    cbar = plt.colorbar()
    cbar.set_label(intensity_name)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/" + plot_name + ".pdf",
        format='pdf', pad_inches=0,  bbox_inches='tight', dpi=1200)
    if show: plt.show()

def plot_connectivity_matrix_binarized(matrix, title, plot_name, show=False):
    plt.clf()
    plt.imshow(matrix, cmap='binary', interpolation='nearest')
    plt.title(title, fontsize=17)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/" + plot_name + ".pdf",
        format='pdf', pad_inches=0, bbox_inches='tight', dpi=1200)
    if show: plt.show()


