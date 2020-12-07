## Second Project for Network Science Course

This repository contains the code mentioned in the report which can be found *here*.

### Dependencies

* bctpy:  ```$pip install bctpy```
* cdlib:  ```$pip install cdlib```
* scipy:  ```$pip install scipy```
* pandas:  ```$pip install pandas```
* matplotlib: ```$pip install matplotlib```

Tested in python 3.7
### Organization

/BrainConnectivityToolboxWrapper/
*  Contains code to compute multiple metrics. 
* More information on its own README file.

/data/pre-processed/
* The original data

/data/processed/
* Data after some transformations for our usage (file process.py). Includes edge list and matrices.
* Also includes some templates:
    * lobes.node: division of each lobe by color.
    * communities_template.node: coordinates of each of the 68 nodes.
    * template.node: template based on the Desikan atlas.


/DesikanViz/
* Populates the Desikan template for visualization.

/reports/
* Includes code to generate bar charts, box plots and scatter plots (plots.py).

Remaining folders are for saving the analysis results and statistics.

### How to use

Run: ```$python main.py```  from root directory.

Parameters of function ```analyse``` may be changed, to select which metrics to run:

```
    degree_centrality = True/False
    node_strength = True/False,
    clustering_coeff = True/False,
    weighted_clustering_coeff = True/False,
    average_path_len = True/False,
    betweenness_centrality = True/False,
    newman_modularity = True/False,
    edge_betweenness = True/False,
    rich_club = True/False,
    participation_coefficient = True/False,
    communities_algorithm=
        'all'/'louvain'/'spinglass'/'walktrap'/'girvan_newman'/'infomap'
    desikan_metric=
        set this parameter with a node metric. (stats file header column)
```

### Authors

* João Coelho
* João Saraiva

