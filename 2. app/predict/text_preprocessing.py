# Load necessary libraries and methods for text cleaning
from bs4 import BeautifulSoup
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Functions for cleaning text

# Use this to deal with apostophes and abbreviation
def remove_apostrophe_abbrev(text):
    return re.sub('[^\w\s]','', text)

# Function to remove stopwords
def remove_stop_words(text):
    clean_text = []
    stop_words = stopwords.words('english')
    for word in text.split():
        if word.strip().lower() not in stop_words:
            clean_text.append(word)

    return " ".join(clean_text)

# Remove html tags, using regex is bad idea
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# Remove links in text, http and https
# s? in regex means or s (case sensitive)
def remove_links(text):
    return re.sub('https?:\/\/\S+', '', text)

# Remove 's (possessive pronouns) from text
# Two kinds of apostophes found
def remove_possessive_pronoun(text):
    return re.sub("’s|'s", '', text)

# Remove between brackets and their contents
def remove_between_brackets(text):
    return re.sub('\([^]]*\)', '', text)

# Remove square brackets and their contents
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

# Remove curly brackets and their contents
# Useful to remove any JavaScript scripts, though removed
# through html as above
def remove_between_curly_brackets(text):
    return re.sub('\{[^]]*\}', '', text)

def remove_n_space(text):
    return re.sub('\n', ' ', text)

# Function to clean text in text column
def text_cleaner(text):
    text = remove_html_tags(text)
    text = remove_links(text)
    text = remove_possessive_pronoun(text)
    text = remove_apostrophe_abbrev(text)
    text = remove_between_brackets(text)
    text = remove_between_square_brackets(text)
    text = remove_between_curly_brackets(text)
    text = remove_n_space(text)
    text = remove_stop_words(text)

    return text

# Function to perform lemmatization on text
def lemmatize_text(text):
    lemma = WordNetLemmatizer()
    tokenize_text = word_tokenize(text)
    lemmatize_words = [lemma.lemmatize(word) for word in tokenize_text]
    join_text = ' '.join(lemmatize_words)

    return join_text

# Final text output
def text_pipe(text):
    text = text_cleaner(text)
    text = lemmatize_text(text)

    return text
