# This script was used to preprocess the data but including numbers and some punctuations marks for the sake of generating meaningful Word Trees

# Import required libraries
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import re
import os


new_working_directory = "/Users/fatimaq/Documents/Qualitative_reddit_analysis/Output"
os.chdir(new_working_directory)


# LOAD DATA ==>

# Create SQL engine to retrieve the data from Table "A" and "B" in reddit.db database
# First provide path of the local reddit.db file;


# Then initiate the SQL engine
engine = create_engine(
    f"sqlite:////Users/fatimaq/Documents/Qualitative_reddit_analysis/Output/testredditpost.sqlite")


# Retrieve data from database into a dataframe "posts" and make it ready for preprocessing
postsA = pd.read_sql("""select * from my_table order by createdAt""", engine)
postsA['id'] = postsA['id'].astype(str) + "A"
posts = pd.concat([postsA])
posts['date'] = posts['createdAt'].str[:10]
posts.set_index('date', inplace=True)
postsA = None


# PREPROCESSING ==>

# Concatenate the text from "title" and "main body" of the reddit posts
posts['text'] = posts['body']
print(posts.head())

# Define a list of punctuation marks that are not required for our use case
puncts = ['"', ':', ')', '(', '-', '!', ',', ';', '|', "'", '/', '[', ']', '>', '=', '#', '*', '+', '\\', '•',  '~', '@',
          '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '™', '›',  '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…',
          '“', '★', '”', '–', '●', 'â', '►', '−', '²', '¬', '░', '¶', '↑', '±', '¿', '▾', '═', '¦', '║', '―', '▓', '—', '‹', '─',
          '▒', '：', '¼', '⊕', '▼', '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲', 'è', '¸', '¾', 'Ã', '⋅', '‘', '∞',
          '∙', '）', '↓', '、', '│', '（', '»', '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø', '¹', '≤', '‡', '√']

# Function to replace punctuation marks with whitespace


def clean_text(x):
    x = str(x)
    for punct in puncts:
        if punct in x:
            x = x.replace(punct, ' ')
    return x


# Remove URL's from posts
posts['clean_text'] = posts['text'].apply(lambda x: re.sub(r'http\S+', '', x))

# Remove punctuation marks
posts['clean_text'] = posts['clean_text'].apply(lambda x: clean_text(x))

# Remove numbers
#posts['clean_text'] = posts['clean_text'].str.replace("[0-9]", " ")

# Remove whitespaces
posts['clean_text'] = posts['clean_text'].apply(lambda x: ' '.join(x.split()))

# Convert text to lowercase
posts['clean_text'] = posts['clean_text'].str.lower()

# Drop duplicates
posts.drop_duplicates(['clean_text'], inplace=True)

print("Total number of unique posts: ", len(posts))
print(posts.head())

# Save a copy of the preprocessed data to be used in other scripts of the project later on
posts.to_csv("PreProcessedDataWithNumbers.csv")
