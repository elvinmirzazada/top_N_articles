# Top Articles by Number of Comments (Non-Async Version)

This project fetches articles from the API and returns the titles of the top N articles with the most comments, in descending order of the number of comments.

## Requirements

- Python 3.7+

## Installation

1. Clone the repository or download the script.
2. Navigate to the directory where the script is located.
3. Install the required dependencies using `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Save the script as `top_articles.py`.
2. Run the script:

    ```sh
    python top_articles.py
    ```

## Explanation

- `fetch_all_articles()`: Fetches all articles from all available pages of the API.
- `filter_and_sort_articles(articles)`: Filters articles to only include those with a title or story title, and sorts them by the number of comments in descending order.
- `get_top_n_articles(articles)`: Retrieves the top N articles with the most comments and extracts their titles.
- `main()`: The main function to fetch, filter, sort, and print the top 10 articles by the number of comments. Also measures the execution time.

## Example Output

```
Total pages to fetch: 5
Top 10 Articles by Number of Comments:
1. UK votes to leave EU - 2531
2. F.C.C. Repeals Net Neutrality Rules - 1397
3. EU approves internet copyright law, including ‘link tax’ and ‘upload filter’ - 1010
4. Switch from Chrome to Firefox - 981
5. W3C abandons consensus, standardizes DRM, EFF resigns - 978
6. Tim Cook Speaks Up - 974
7. A Message to Our Customers - 967
8. Don't Fly During Ramadan - 961
9. SpaceX’s Falcon Heavy successfully launches - 872
10. macOS High Sierra: Anyone can login as “root” with empty password - 813

Execution time: 4.083693504333496 seconds
```


## License

This project is licensed under the MIT License.
