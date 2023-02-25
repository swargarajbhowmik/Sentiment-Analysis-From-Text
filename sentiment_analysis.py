# Importing Dependencies
from textblob import TextBlob

# Defining The String
data = "I"

# Creating The Blob Object
blob = TextBlob(data)
polarity = blob.sentiment.polarity

# Finding Sentiment
if polarity > 0:
    print("The Text is Positive")
elif polarity < 0:
    print("The Text is Negative")
else:
    print("The Text is Neutral")