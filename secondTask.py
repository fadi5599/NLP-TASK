import pandas as pd
import nltk
from nltk.stem import PorterStemmer

# Download necessary NLTK resources if you haven't already
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset from Kaggle 
# IMDB dataset having 50K movie reviews for natural language processing or Text analytics.
df = pd.read_csv('IMDB Dataset.csv')  

# Create a PorterStemmer object
stemmer = PorterStemmer()

# Function to perform tokenization and stemming
def process_text(text):
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Apply the processing function to the 'sentiment' column of the DataFrame
df['processed_text'] = df['sentiment'].apply(process_text)  

# Print the first few rows of the processed DataFrame
print(df.head())