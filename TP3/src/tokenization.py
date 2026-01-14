import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text_lower = text.lower()
    text_no_punct = "".join([char for char in text_lower if char not in string.punctuation])
    tokens = text_no_punct.split(" ")
    clean = [word for word in tokens if word not in stop_words]
    return(clean)



