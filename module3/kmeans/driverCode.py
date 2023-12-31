import pandas as pd
import elbowMethod
import clusterQuality.silhouetteAnalysis as silhouetteAnalysis
import kmeans
from plotting.brandAffinityPerCluster import brandAffinityPerCluster
from plotting.prodCatPerCluster import productCategoryPerCluster
from plotting.scatter3D import scatter3DPlot
# Load the data
data = pd.read_csv('transformations/normalization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
original_data = data.copy()
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data = data.drop(columns=columns_to_drop)
def kMeansDriverCode(data, original_data):
    # Apply Elbow Method
    elbowMethod.elbowMethod(data)

    # Apply Silhouette Analysis
    silhouetteAnalysis.silhouetteAnalysis(clustering_data=data)

    # K-Means
    data = kmeans.kMeansAlgorithm(data, clustering_data=original_data, clusters=5)

    # Plotting 
    brandAffinityPerCluster(data)
    productCategoryPerCluster(data)
    scatter3DPlot(data)

kMeansDriverCode(data, original_data)