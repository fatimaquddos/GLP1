

# This script was used to generate Important Features

# Import required libraries
from csv import writer
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
import os
nltk.download('stopwords')
# Set the working directory if needed
new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)
 


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize

# Create a funtion to preprocess the nltk tokenized dataframe

 
# Load lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))
# Load the cleaned data from "PreProcessedData.csv" file
df = pd.read_csv("PreProcessedData.csv")

def word_tokenizer(text):
    tokenized_text = text
    tokenized_text_proc = [token.lower() for token in tokenized_text 
                           if  (not token.lower() in stopwords) # Remove stopwords 
                           and (not len(token) <= 2)]     # Remove short tokens
    tokenized_text_proc = [lemmatizer.lemmatize(token) for token in tokenized_text_proc]
    return tokenized_text_proc



def getImportantFeatures(sampNo=1):
    # Load the final labels and merge with preprocessed data
    sample = pd.read_csv(f"FinalLabelsSample{sampNo}.csv")

    # Create an excel file to save important features for each cluster
    writer = pd.ExcelWriter(f"ImportantFeaturesSample{sampNo}.xlsx", engine='xlsxwriter')

    # Merge dataframes and set date as index
    temp = df.merge(sample, how='inner', left_on='id', right_on='ids')
    temp['clean_text'] = temp['clean_text'].astype(str)
    temp['date'] = pd.to_datetime(temp['date'])
    temp.set_index('date', inplace=True)
    # Tokenize the clean text
    temp['tokens'] = temp['clean_text'].apply(word_tokenize)
    temp['tokens'] = temp['tokens'].apply(word_tokenizer)

    cv = TfidfVectorizer(lowercase=False, tokenizer=lambda x:x, max_features=500)
    cv_matrix = cv.fit_transform(temp['tokens'])
    
    
    # Run the loop for each cluster and save the generated Important Features in excel file
    for i in range(1,9):
        print("\n=========================================")
        temp1 = temp.copy()        

        
        # Script to create arrays to map binary cluster
        start, stop, restart_point = i, i-1, 8
        if stop < start:
            stop += restart_point
        clusterNo = []
        for i in range(start-1, stop):
            val = i % restart_point + 1
            clusterNo.append(val)
        
        
        # Map the binary cluster
        temp1[f"Binary Cluster {clusterNo[0]}"] = temp1['labels'].map({clusterNo[0]:1, clusterNo[1]:0, clusterNo[2]:0, clusterNo[3]:0, clusterNo[4]:0, clusterNo[5]:0, clusterNo[6]:0, clusterNo[7]:0})
        print()
        print(f"Training binary classifier for Cluster {clusterNo[0]}\n",temp1[f"Binary Cluster {clusterNo[0]}"].value_counts())

        # Train the Supervised learning model
        clf = RandomForestClassifier(random_state=47)
        clf.fit(cv_matrix, temp1[f"Binary Cluster {clusterNo[0]}"].values)

        # Sort the features w.r.t. their importance weight
        sorted_feature_weight_idxes = np.argsort(clf.feature_importances_)[::-1]
        most_important_features = np.take_along_axis(np.array(cv.get_feature_names_out()), sorted_feature_weight_idxes, axis=0)
        most_important_weights = np.take_along_axis(np.array(clf.feature_importances_), sorted_feature_weight_idxes, axis=0)
        print(f"\nSample {sampNo}, Cluster {clusterNo[0]} - Important Features with weights\n",list(zip(most_important_features, most_important_weights))[:10])
        
        # Write the featurs dataframe to local disk
        featuredf = pd.DataFrame(list(zip(most_important_features, most_important_weights))[:50], columns=['feature','weight'])
        featuredf.to_excel(writer, sheet_name=f'Cluster{clusterNo[0]}', index=True)
        
    # Save the excel file
    writer._save()
    

# Run the function to generate important features list for Sample 1    
getImportantFeatures()