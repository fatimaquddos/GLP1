import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

# Set the working directory if needed
new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Load Sample 1 embeddings obtained from the previous step
df = pd.read_csv("Sample1Embeddings.csv")

# Check the format of the embeddings data; identified as "str" in this case
print(type(df["embeddings"][0]))

# Convert the "str" format of the embeddings to "list" format to be used as input in clustering algorithm
X = df["embeddings"].apply(lambda x: list(map(float, x.strip('][').split(', ')))).tolist()

X = np.array(X)

# Check the format of the embeddings data; should be "list" in this case
print(type(X[0]))


# Import ElbowVisualizer
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,30), timings= True)
visualizer.fit(X)        # Fit data to visualizer
visualizer.show()        # Finalize and render figure

## 10 clusters

# Add the cluster labels to the DataFrame
visualizer["labels"] = model.labels_

# Select the columns to be exported
df = visualizer[["ids", "labels"]]

# Save the output to a new CSV file
df.to_csv("KmeansLabelsSample1.csv", index=False)
