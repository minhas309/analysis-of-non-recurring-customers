import pandas as pd
import elbowMethod
import clusterQuality.silhouetteAnalysis as silhouetteAnalysis
import kmeans
from plotting.brandAffinityPerCluster import brandAffinityPerCluster
from plotting.prodCatPerCluster import productCategoryPerCluster
from plotting.scatter3D import scatter3DPlot
# Load the data
data = pd.read_csv('transformations/normalization.csv')
columns_to_cluster = ['mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score', 'mAverage_Spending_Per_Purchase', 'mPurchase_Amount']
clustering_data = data[columns_to_cluster]

def kMeansDriverCode(data, cluster_data):
    # Apply Elbow Method
    elbowMethod.elbowMethod(cluster_data)

    # Apply Silhouette Analysis
    silhouetteAnalysis.silhouetteAnalysis(clustering_data=cluster_data)

    # K-Means
    data = kmeans.kMeansAlgorithm(data, clustering_data=cluster_data, clusters=6)

    # Plotting 
    brandAffinityPerCluster(data)
    productCategoryPerCluster(data)
    scatter3DPlot(data)

kMeansDriverCode(data, clustering_data)