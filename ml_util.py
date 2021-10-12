import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def understanding(df):
    print(df.info())
    print(df.describe())
    for col in df.columns:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            plt.hist(df[col])
            plt.title(col)
            plt.show()
            plt.clf()
        elif df[col].dtype == 'object':
            sns.barplot(df[col].value_counts().index,df[col].value_counts()).set_title(col)
            plt.show()
            
def heat(df):
    num_columns = []
    for col in df.columns:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            num_columns.append(col)
    sns.heatmap(df[num_columns].corr(), annot=True)
    
def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr