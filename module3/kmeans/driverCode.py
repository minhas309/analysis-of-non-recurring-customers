import pandas as pd
import elbowMethod
import clusterQuality.silhouetteAnalysis as silhouetteAnalysis
import kmeanspp
from plotting.brandAffinityPerCluster import brandAffinityPerCluster
from plotting.prodCatPerCluster import productCategoryPerCluster
from plotting.scatter3D import scatter3DPlot
# Load the data 
data = pd.read_csv('transformations/normalization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
original_data = data.copy()
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data = data.drop(columns=columns_to_drop)

data_dataset = pd.read_csv('cleaned/data.csv')
def kMeansDriverCode(data, original_data):
    # Apply Elbow Method
    elbowMethod.elbowMethod(data)

    # Apply Silhouette Analysis
    silhouetteAnalysis.silhouetteAnalysis(clustering_data=data)

    # K-Means
    data = kmeanspp.kMeansAlgorithmPP(data, clustering_data=original_data, clusters=5)
    data_dataset['cluster'] = data['Cluster']
    data_dataset.to_csv('cleaned/data.csv', index=False)

    # Plotting 
    brandAffinityPerCluster(data)
    productCategoryPerCluster(data)

kMeansDriverCode(data, original_data)