# This script was used to merge and further optimize the number of Clusters based on underlying keywords and domain knowledge
# The optimum clusters, obtained after applying the Elbow method in scripts "5a, 5b & 5c", were further merged and their number was reduced from 20 to 12

# Import required libraries
import pandas as pd
import os

new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)



# SAMPLE 1 relabeling for 12 Optimized Clusters
df = pd.read_csv("KmeansLabelsSample1.csv")

df.loc[df['labels'] == 0, ['labels']] = 41
df.loc[df['labels'] == 1, ['labels']] = 42
df.loc[df['labels'] == 5, ['labels']] = 42
df.loc[df['labels'] == 7, ['labels']] = 42
df.loc[df['labels'] == 2, ['labels']] = 43
df.loc[df['labels'] == 3, ['labels']] = 43
df.loc[df['labels'] == 8, ['labels']] = 43
df.loc[df['labels'] == 4, ['labels']] = 44
df.loc[df['labels'] == 9, ['labels']] = 44
df.loc[df['labels'] == 6, ['labels']] = 45
df.loc[df['labels'] == 10, ['labels']] = 46
df.loc[df['labels'] == 11, ['labels']] = 47
df.loc[df['labels'] == 12, ['labels']] = 48


df.loc[df['labels'] == 41, ['labels']] = 1
df.loc[df['labels'] == 42, ['labels']] = 2
df.loc[df['labels'] == 43, ['labels']] = 3
df.loc[df['labels'] == 44, ['labels']] = 4
df.loc[df['labels'] == 45, ['labels']] = 5
df.loc[df['labels'] == 46, ['labels']] = 6
df.loc[df['labels'] == 47, ['labels']] = 7
df.loc[df['labels'] == 48, ['labels']] = 8

# Check the labels and their respective counts to confirm the correct changes for sample 1
print(df['labels'].value_counts())

# Save the Final cluster labels to the local disk
df.to_csv("FinalLabelsSample1.csv", index=False)
