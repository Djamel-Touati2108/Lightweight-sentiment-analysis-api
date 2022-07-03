import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def start_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    s=sid.polarity_scores(text)
    if s['compound']> 0: return "positive"
    elif s['compound'] < 0 : return "negative"
    else: return "neutral"