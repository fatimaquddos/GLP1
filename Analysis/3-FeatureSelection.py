import pandas as pd
import tensorflow_hub as hub
import json
import numpy as np
import os

# Set the working directory if needed

new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)

# Load the cleaned data from "PreProcessedData.csv" file
posts = pd.read_csv("PreProcessedData.csv")
posts["date"] = pd.to_datetime(posts["date"])

# FEATURE SELECTION | Retrieve USE EMBEDDINGS for each cleaned text post ==>

# Load the latest model of pretrained USE encoder from Tensorflow Hub
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)

# Function to obtain output from the USE model for a given text input
def embed(input):
    input = list(map(str, input))
    return model(input)

# Obtain embeddings for all posts at once
embeddings = embed(posts['clean_text'])

# Create a dictionary to store the "ids" and corresponding "embeddings" for each text post
data = {
    "ids": posts['id'].values.tolist(),
    "embeddings": np.array(embeddings).tolist()
}

# Save the data in a JSON file
with open("Embeddings1.json", "w") as fp:
    json.dump(data, fp, indent=4)
