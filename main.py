import requests
from textblob import TextBlob

NEWS_API_KEY = "YOUR_NEWS_API_KEY"

def get_headlines(query="bitcoin"):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    return [a["title"] for a in articles[:10]]

def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    return round(sentiment, 3)

def run():
    print("🔍 Market Sentiment Analyzer — AI Powered\n")
    keyword = input("Enter a market keyword (e.g., bitcoin, stocks, inflation): ")

    headlines = get_headlines(keyword)

    if not headlines:
        print("No news found. Try another keyword.")
        return

    total_score = 0
    print("\nTop Headlines Sentiment:\n")

    for h in headlines:
        score = analyze_sentiment(h)
        total_score += score
        print(f"📰 {h}\n➡ Sentiment Score: {score}\n")

    avg_score = round(total_score / len(headlines), 3)
    print("\n📊 Final Market Sentiment Score:", avg_score)

if __name__ == "__main__":
    run()
