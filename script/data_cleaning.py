
import numpy as np 
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
pd.set_option('max_column', None)



df = pd.csv('df')


# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):
     # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The Diabetes dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

percent_missing(df)


#fix the missing values
def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]

def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]




