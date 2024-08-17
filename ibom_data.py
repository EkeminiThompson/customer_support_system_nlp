# data_preprocessing.py
import pandas as pd
import nltk
from sklearn.model_selection import train_test_split

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load the data
data = pd.read_csv('customer_support_data.csv')

# Preprocess the text data
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    lemmatizer = nltk.WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens])

data['query'] = data['query'].apply(preprocess_text)

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Save the preprocessed data
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
