# Import required libraries
import pandas as pd
import umap
import os

# Set the working directory if needed
new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)

# Define a function to run UMAP algorithm on Sample 1
def runUMAP():
    # Load embeddings obtained from script "4b"
    df = pd.read_csv("Sample1Embeddings.csv")

    # Check the format of the embeddings data; identified as "str" in this case
    print(type(df["embeddings"][0]))

    # Convert the "str" format of the embeddings to "list" format to be used as an input in the model
    X = df["embeddings"].apply(lambda x: list(map(float, x.strip('][').split(', ')))).tolist()

    # Check the format of the embeddings data; should be "list" in this case
    print(type(X[0]))

    # Fit the data to UMAP model to obtain 2 components representing 512D embeddings in a 2D space
    embedding = umap.UMAP(n_neighbors=4, verbose=True, low_memory=True, n_jobs=-1, n_epochs=2000).fit_transform(X)

    # Add the two UMAP components to the dataframe
    df["UMAPx"] = embedding[:, 0]
    df["UMAPy"] = embedding[:, 1]

    # Select the columns to be exported
    df = df[["ids", "UMAPx", "UMAPy"]]

    # Import final labels
    dff = pd.read_csv("FinalLabelsSample1.csv")

    # Merge the two dataframes
    dff = dff.merge(df, how="inner", on="ids")

    # Save the output to local disk
    dff.to_csv("UMAPComponentsSample1.csv", index=False)

# Run the function for Sample 1 and receive the 2 UMAP components in the output file "UMAPComponentsSample1.csv" on local disk in CSV format
runUMAP()
