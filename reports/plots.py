import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import powerlaw
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from numpy import polyfit
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

def create_plot_communitycolored(path_to_save: str, title: str, xlabel: str, xdata: list, ylabel: str, ydata: list, xticks:list = None, yticks: list = None,
                                 communities=None):

    fig = plt.figure()
    fig.set_size_inches(14.0, 14.0)
    ax = plt.subplot(1, 1, 1)

    colors = ['#FF011D', '#FFB400', '#69BF23', '#00B3CE', '#2E36AD', '#fa007d', '#FF7F00']

    max = np.max(communities) + 1

    communities = np.where(communities == 0, colors[0], communities)
    for i in range(1, max):
        communities = np.where(communities == str(i), colors[i], communities)

    print(communities)
    plt.scatter(xdata, ydata, color=communities)


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

    fig.savefig(path_to_save, bbox_inches='tight', pad_inches=0)

    return

def create_plot_lobecolored(path_to_save: str, title: str, xlabel: str, xdata: list, ylabel: str, ydata: list, xticks:list = None, yticks: list = None, discrete=True,
                            also_log_scale: bool = False, log_yticks: list = None, powerlaw_xmin=None, powerlaw_xmax=None, xforplaw=None):

    template = pd.read_csv("data/lobes.node", " ", header='infer')
    colors = template["Color"].tolist()
    grouped_template = template.groupby('Lobe')  # mergesort is stable, i.e, preserves the original order

    fig = plt.figure()
    fig.set_size_inches(14.0, 14.0)

    # Plot in linear scale
    ax = plt.subplot(2 if also_log_scale else 1, 1, 1)
    plt.scatter(xdata, ydata, color=colors)
    for i in range(1, 8):
        group_indexes = grouped_template.get_group(i).index.tolist()
        sub_xdata, sub_ydata = [], []
        for ix in group_indexes:
            sub_xdata.append(xdata[ix])
            sub_ydata.append(ydata[ix])
        m, b = polyfit(sub_xdata, sub_ydata, 1)
        plt.plot(xdata, m*xdata + b, color=grouped_template.get_group(i)['Color'].tolist()[0], linestyle='--')

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
    if xbins:
        ax.xaxis.set_ticks(xbins)
    if yticks:
        ax.yaxis.set_ticks(yticks)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, axis='y')

    fig.savefig(path_to_save, bbox_inches = 'tight',
    pad_inches = 0)
    return


def create_bar_lobe_grouped(path_to_save: str, title: str,
               ylabel: str, ydata: list,
               xbins:list = None, yticks: list = None):

    template = pd.read_csv("data/lobes.node", " ", header='infer')
    sorted_template = template.sort_values('Lobe',kind='mergesort') # mergesort is stable, i.e, preserves the original order
    colors = sorted_template["Color"].tolist()
    rois = sorted_template["RegionName"].tolist()

    grouped_ydata = []
    for ix in sorted_template.index:
        grouped_ydata.append(ydata[ix])

    fig = plt.figure()
    fig.set_size_inches(10.0, 7.0)
    ax = plt.subplot(1, 1, 1)

    plt.bar(rois, grouped_ydata, color=colors)

    plt.title(title)
    plt.xlabel('ROI', fontsize=12)
    plt.ylabel(ylabel, fontsize=18)
    if xbins:
        ax.xaxis.set_ticks(xbins)
    if yticks:
        ax.yaxis.set_ticks(yticks)
    plt.xticks(fontsize=9, rotation='vertical')
    plt.yticks(fontsize=16)
    plt.grid(True, axis='y')

    fig.savefig(path_to_save, bbox_inches='tight',
                pad_inches=0)
    return


def create_bar_hemisphere_grouped(path_to_save: str, title: str,
               ylabel: str, ydata: list,
               xbins:list = None, yticks: list = None):

    template = pd.read_csv("data/lobes.node", " ", header='infer')
    sorted_template_left = template[0:34].sort_values('Lobe',kind='mergesort') # mergesort is stable, i.e, preserves the original order
    sorted_template_right = template[34:69].sort_values('Lobe', kind='mergesort')
    colors = sorted_template_left["Color"].tolist() + sorted_template_right["Color"].tolist()
    rois = sorted_template_left["RegionName"].tolist() + sorted_template_right["RegionName"].tolist()

    grouped_ydata = []
    for ix in sorted_template_left.index:
        grouped_ydata.append(ydata[ix])
    for ix in sorted_template_right.index:
        grouped_ydata.append(ydata[ix])

    fig = plt.figure()
    fig.set_size_inches(10.0, 7.0)
    ax = plt.subplot(1, 1, 1)

    plt.bar(rois, grouped_ydata, color=colors)

    plt.title(title)
    plt.xlabel('ROI', fontsize=12)
    plt.ylabel(ylabel, fontsize=18)
    if xbins:
        ax.xaxis.set_ticks(xbins)
    if yticks:
        ax.yaxis.set_ticks(yticks)
    plt.xticks(fontsize=9, rotation='vertical')
    plt.yticks(fontsize=16)
    plt.grid(True, axis='y')

    fig.savefig(path_to_save, bbox_inches='tight',
                pad_inches=0)
    return

def create_bar_lobe_grouped_descending(path_to_save: str, title: str,
               ylabel: str, ydata: list,
               xbins:list = None, yticks: list = None):

    template = pd.read_csv("data/lobes.node", " ", header='infer')
    indexes = template.index.tolist()
    data = dict()
    for i in range(len(indexes)):
        data[indexes[i]] = ydata[i]

    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

    colors = list()
    for i in sorted_data.keys():
        colors.append((template.loc[[i]]['Color']).tolist()[0])


    rois = list()
    for i in sorted_data.keys():
        rois.append(template.loc[[i]]['RegionName'].tolist()[0])

    fig = plt.figure()
    fig.set_size_inches(10.0, 4.0)
    ax = plt.subplot(1, 1, 1)

    plt.bar(rois, sorted_data.values(), color=colors)

    plt.title(title)
    plt.xlabel('ROI', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    if xbins:
        ax.xaxis.set_ticks(xbins)
    if yticks:
        ax.yaxis.set_ticks(yticks)
    plt.xticks(fontsize=9, rotation='vertical')
    plt.yticks(fontsize=16)
    plt.grid(True, axis='y')

    fig.savefig(path_to_save, bbox_inches='tight',
                pad_inches=0)
    return


def create_box_plot(arg):

    df = pd.read_csv("stats/EDGE-stats-fmri", sep='\t')


    rich_subset = df.loc[df['EdgeType'] == 'rich'][arg].to_list()
    periphery_subset = df.loc[df['EdgeType'] == 'periphery'][arg].to_list()
    feeder_subset = df.loc[df['EdgeType'] == 'feeder'][arg].to_list()

    data = [rich_subset, periphery_subset, feeder_subset]

    plt.boxplot(data)

    plt.xlabel(['rich', 'periphery', 'feeder'])

    plt.show()

def create_communities_table(communities_per_algorithm, names):
    colors = None
    for i in range(len(communities_per_algorithm)):
        cols = communities_per_algorithm[i]
        norm = plt.Normalize(cols.min() - 1, cols.max() + 1)
        colors_new = plt.cm.cool(norm(cols))
        if colors is None:
            colors  = colors_new
        else:
            colors = np.concatenate([colors, colors_new], 0)
        print(colors)

    print(colors)
    fig = plt.figure(figsize=(5, 2))
    plt.axis('off')
    plt.table(np.empty((5,68), str), rowLabels=names, colLabels=list(range(0,68)), loc='center',
                  cellColours=colors, colWidths=[0.1] * 5)

    plt.title("Communities per algorithm", fontsize=8)

    plt.show()
    fig.savefig("reports/tables/communities.pdf", bbox_inches='tight', pad_inches=0)
