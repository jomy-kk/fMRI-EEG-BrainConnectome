import pandas as pd


# metric: list of 68 values
# name: name of the metric
def write_desikan(name_metric, name_matrix, metric):
    df = pd.read_csv("data/template.node", sep=' ', skiprows=1, names=['c1', 'c2', 'c3', 'lobo', 'metric', 'label'])

    df['metric'] = metric

    df.to_csv("DesikanViz/files/desikan-" + name_matrix + "-" + name_metric+".node", sep=' ', index=False, header=False)