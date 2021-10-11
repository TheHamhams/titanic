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
            
