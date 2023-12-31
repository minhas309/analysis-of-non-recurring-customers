import pandas as pd
import algorithm
from plotting.algoPlot import algorithmPlot
# Load the data
data = pd.read_csv('transformations/normalization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data = data.drop(columns=columns_to_drop)
def dbScanDriverCode(data):
    eps_values = [0.1,0.3,0.5]
    min_samples_values = [1,2]
    for eps in eps_values:
        for min_sampless in min_samples_values:
            print("Sampling sample", eps, min_sampless)
            algorithm.dbScanAlgorithm(data=data, eps=eps, min_samples=min_sampless)
    
    algorithmPlot(data=data, eps=0.5, min_samples=1)

dbScanDriverCode(data)
