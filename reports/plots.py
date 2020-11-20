import matplotlib.pyplot as plt
import matplotlib as mpl
import powerlaw
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



##################################################
################# MATRICES #######################
##################################################

def plot_connectivity_matrix(matrix, intensity_name, title, plot_name, show=False):
    plt.clf()
    plt.imshow(matrix, cmap='jet', interpolation='nearest')
    plt.title(title, fontsize=17)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    cbar = plt.colorbar()
    cbar.set_label(intensity_name)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/matrices/" + plot_name + ".pdf",
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
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/matrices/" + plot_name + ".pdf",
        format='pdf', pad_inches=0,  bbox_inches='tight', dpi=1200)
    if show: plt.show()

def plot_connectivity_matrix_binarized(matrix, title, plot_name, show=False):
    plt.clf()
    plt.imshow(matrix, cmap='binary', interpolation='nearest')
    plt.title(title, fontsize=17)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.savefig(
        "/Users/jomy/OneDrive - Universidade de Lisboa/9º Semestre/CRC - Ciência das Redes Complexas/project2/reports/plots/matrices/" + plot_name + ".pdf",
        format='pdf', pad_inches=0, bbox_inches='tight', dpi=1200)
    if show: plt.show()



##################################################
################## METRICS #######################
##################################################

def create_plot(path_to_save: str, title: str, xlabel: str, xdata: list, ylabel: str, ydata: list, xticks:list = None, yticks: list = None, discrete=True,
                also_log_scale: bool = False, log_yticks: list = None, powerlaw_xmin=None, powerlaw_xmax=None, xforplaw=None):
    fig = plt.figure()
    fig.set_size_inches(14.0, 14.0)

    # Plot in linear scale
    ax = plt.subplot(2 if also_log_scale else 1, 1, 1)
    plt.scatter(xdata, ydata)
    #plt.title(title + ' (linear scale)' if also_log_scale else '')
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    ax.set_xscale('linear')
    ax.set_yscale('linear')
    if yticks:
        ax.set_ylim(ymin=yticks[0], ymax=yticks[len(yticks) - 1])
        ax.set_yticks(yticks)
    if xticks:
        ax.set_xlim(xmin=xticks[0], xmax=xticks[len(xticks) - 1])
        ax.set_xticks(xticks)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()


    # Plot in log scale
    if also_log_scale:
        ax = plt.subplot(2, 1, 2)
        plt.scatter(xdata, ydata)
        #plt.title(title + ' (log scale)')
        plt.xlabel('log(' + xlabel + ')', fontsize=18)
        plt.ylabel('log(' + ylabel + ')', fontsize=18)
        ax.set_xscale('log')
        ax.set_yscale('log')
        if log_yticks:
            ax.set_ylim(ymin=log_yticks[0], ymax=log_yticks[len(log_yticks)-1])
            ax.set_yticks(log_yticks)
        ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
        plt.grid()


        # Plot power law
        if powerlaw_xmin and powerlaw_xmax:
            fit = powerlaw.Fit(xforplaw , xmin=powerlaw_xmin, xmax=powerlaw_xmax, discrete=discrete)
        else:
            fit = powerlaw.Fit(xforplaw , discrete=True)

        fit.power_law.plot_pdf(color='r', linestyle='--', label='fit pdf')

        fig.savefig(path_to_save, bbox_inches = 'tight',
    pad_inches = 0)
        return fit.power_law.alpha

    fig.savefig(path_to_save, bbox_inches = 'tight',
    pad_inches = 0)
    return


def create_bar(path_to_save: str, title: str,
               xlabel: str, xdata: list,
               ylabel: str, ydata: list,
               xbins:list = None, yticks: list = None):

    fig = plt.figure()
    fig.set_size_inches(10.0, 7.0)
    ax = plt.subplot(1, 1, 1)
    plt.bar(xdata, ydata)
    plt.title(title)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    ax.xaxis.set_ticks(xbins)
    ax.yaxis.set_ticks(yticks)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, axis='y')

    fig.savefig(path_to_save, bbox_inches = 'tight',
    pad_inches = 0)
    return
