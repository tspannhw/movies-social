
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys

def predict_sentiment(args):
    sentence = args.get('sentence')
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    sentiment = "positive"
    if ss['compound'] == 0.00:
      sentiment = 'neutral'
    elif ss['compound'] < 0.00:
      sentiment = 'negative'
      
    return sentiment
