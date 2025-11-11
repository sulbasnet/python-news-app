import requests

API = "a50ca0f2b35444cd8b13fab8fad10e41" 
URL = "https://newsapi.org/v2/"

def headlines(country="us"):
    url = f"{URL}top-headlines"
    params = {"country": country, "apiKey": API}
    response = requests.get(url, params=params)
    data = response.json()
    show_articles(data)

def category_news(category="technology", country="us"):
    url = f"{URL}top-headlines"
    params = {"country": country, "category": category, "apiKey": API}
    response = requests.get(url, params=params)
    data = response.json()
    show_articles(data)

def search_news(keyword):
    url = f"{URL}everything"
    params = {"q": keyword, "apiKey": API, "sortBy": "publishedAt"}
    response = requests.get(url, params=params)
    data = response.json()
    show_articles(data)

def show_articles(data):
    if data.get("status") != "ok":
        print("Error fetching news:", data.get("message"))
        return

    articles = data.get("articles", [])
    if not articles:
        print("No news found.")
        return

    for i, article in enumerate(articles[:10], start=1):
        print(f"\n {i}. {article.get('title')}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Author: {article.get('author', 'N/A')}")
        print(f"   Published: {article.get('publishedAt', '')[:10]}")
        print(f"   URL: {article.get('url')}")
        print("-" * 60)

def main():
    while True:
        print("\n=== Simple News App ===")
        print("1. Top Headlines")
        print("2. Category News")
        print("3. Search News")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            country = input("Enter country code (us, in, gb, np...): ").lower()
            headlines(country)

        elif choice == "2":
            country = input("Enter country code (us, in, gb, np...): ").lower()
            print("Categories: business, entertainment, general, health, science, sports, technology")
            category = input("Enter category: ").lower()
            category_news(category, country)

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            search_news(keyword)

        elif choice == "4":
            print("Stay informed!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
