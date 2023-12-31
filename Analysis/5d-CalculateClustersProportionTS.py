# Proportion of clusters over time to observe if there are any significant movements anywhere

# Import required libraries
import pandas as pd
import os

new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)

# Read the preprocessed data in a dataframe
df = pd.read_csv("PreProcessedData.csv", usecols=["date", "id"])


# Function to calculate proportion of clusters per month between 2008-21
def calProp(sampNo=1):

    sample = pd.read_csv(f"FinalLabelsSample{sampNo}.csv")

    temp = df.merge(sample, how='inner', left_on='id', right_on='ids')
    temp['date'] = pd.to_datetime(temp['date'])
    temp.set_index('date', inplace=True)
    print(len(temp))

    totalCount = temp.resample("M").count()
    TSdf = totalCount[['id']].copy()
    TSdf.rename(columns={'id': 'Total'}, inplace=True)

    for i in range(1, 9):
        clusterdf = temp[temp.labels == i].copy()

        countdf = clusterdf.resample("M").count()
        TSdf = TSdf.join(countdf['id'])
        TSdf.rename(columns={'id': f'{i}'}, inplace=True)

    for i in range(1, 9):
        TSdf[f'pr{i}'] = TSdf[f'{i}']/TSdf['Total']

    TSdf = TSdf[["Total", 'pr1', 'pr2', 'pr3', 'pr4', 'pr5',
                 'pr6', 'pr7', 'pr8']].copy()

    TSdf.to_csv(f"Sample{sampNo}ClustersProportion.csv")


# Calculate proportion of clusters for monthly time series
calProp()
