# Hierarchical Clustering
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


def parse(csv_file, x_axis_col, y_axis_col, csv_folder="csv"):
    dataset = pd.read_csv(csv_folder + "//" + csv_file)
    X = dataset.iloc[:, [x_axis_col, y_axis_col]].values
    return X


def dendrogram(X):
    dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.savefig('hc1.png')
    plt.close()


def hc(X, clusters)
    hc = AgglomerativeClustering(n_clusters = clusters, affinity = 'euclidean', linkage = 'ward')
    y_hc = hc.fit_predict(X)
    plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
    plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
    plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
    plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.savefig('hc2.png')
    plt.close()

