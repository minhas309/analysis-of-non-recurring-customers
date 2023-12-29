import pandas as pd
import algorithm
from plotting.algoPlot import algorithmPlot
# Load the data
data = pd.read_csv('transformations/normalization.csv')
columns_to_cluster = ['mAverage_Spending_Per_Purchase', 'mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score', 'mPurchase_Amount']
clustering_data = data[columns_to_cluster]

def dbScanDriverCode(data, cluster_data):
    eps_values = [ 0.1, 0.2]
    min_samples_values = [1,3,5]
    for eps in eps_values:
        for min_sampless in min_samples_values:
            print("Sampling sample", eps, min_sampless)
            algorithm.dbScanAlgorithm(data=cluster_data, eps=eps, min_samples=min_sampless)
    
    algorithmPlot(data=cluster_data, eps=0.1, min_samples=1)

dbScanDriverCode(data, clustering_data)
