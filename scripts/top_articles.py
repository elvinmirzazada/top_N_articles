import requests
import time

def fetch_all_articles():
    """
    Fetches all articles from all available pages of the API.

    Returns:
        list: A list of all articles.
    """
    base_url = "https://jsonmock.hackerrank.com/api/articles?page="
    page_number = 1
    all_articles = []

    while True:
        response = requests.get(base_url + str(page_number))
        data = response.json()

        # Add the articles from the current page to the all_articles list
        all_articles.extend(data['data'])

        # Check if we have fetched all pages
        if page_number >= data['total_pages']:
            break

        # Move to the next page
        page_number += 1
    print(f"Total pages to fetch: {page_number}")
    return all_articles

def filter_and_sort_articles(articles):
    """
    Filters articles to only include those with a title or story title, and sorts them by the number of comments in descending order.

    Args:
        articles (list): A list of articles.

    Returns:
        list: A sorted list of filtered articles.
    """
    # Filter out articles without a title or story_title
    filtered_articles = [
        article for article in articles
        if article.get('title') or article.get('story_title')
    ]

    # Sort the articles by the number of comments in descending order
    sorted_articles = sorted(filtered_articles, key=lambda x: x['num_comments'] or 0, reverse=True)

    return sorted_articles

def get_top_n_articles(articles, num: int = 10):
    """
    Retrieves the top N articles with the most comments and extracts their titles.

    Args:
        articles (list): A sorted list of articles.
        num (int): Number of top articles, default is 10

    Returns:
        list: A list of titles of the top 10 articles.
    """
    # Get the top 10 articles with the most comments
    top_articles = articles[:num]
    
    # Extract the titles from the top articles
    top_titles = [
        (article.get('title') or article['story_title'], article['num_comments'])
        for article in top_articles
    ]

    return top_titles

def main():
    start_time = time.time()

    # Step 1: Fetch all articles from the API
    all_articles = fetch_all_articles()
    
    # Step 2: Filter and sort articles
    sorted_articles = filter_and_sort_articles(all_articles)
    
    # Step 3: Get the top 10 articles' titles
    top_10_titles = get_top_n_articles(sorted_articles, num=10)
    
    # Print the result
    print("Top 10 Articles by Number of Comments:")
    for i, item in enumerate(top_10_titles, 1):
        print(f"{i}. {item[0]} - {item[1]}")

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
