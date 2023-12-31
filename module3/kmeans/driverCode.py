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
def kMeansDriverCode(data):
    # Apply Elbow Method
    elbowMethod.elbowMethod(data)

    # Apply Silhouette Analysis
    silhouetteAnalysis.silhouetteAnalysis(clustering_data=data)

    # K-Means
    data = kmeans.kMeansAlgorithm(data, clustering_data=data, clusters=3)

    # Plotting 
    brandAffinityPerCluster(data)
    productCategoryPerCluster(data)
    scatter3DPlot(data)

kMeansDriverCode(data)