import unittest
import sys
 
# setting path
sys.path.append('scripts/')
from top_articles import fetch_all_articles, filter_and_sort_articles, get_top_n_articles


class TestTopArticles(unittest.TestCase):
    
    def test_filter_and_sort_articles(self):
        articles = [
            {'title': 'Article 1', 'num_comments': 10},
            {'story_title': 'Article 2', 'num_comments': 20},
        ]
        expected = [
            {'story_title': 'Article 2', 'num_comments': 20},
            {'title': 'Article 1', 'num_comments': 10}
        ]
        result = filter_and_sort_articles(articles)
        self.assertEqual(result, expected)

    def test_get_top_n_articles(self):
        articles = [
            {'title': 'Article 1', 'num_comments': 10},
            {'title': 'Article 2', 'num_comments': 20},
            {'title': 'Article 3', 'num_comments': 5},
        ]
        expected = [('Article 2', 20), ('Article 1', 10), ('Article 3', 5)]
        articles = filter_and_sort_articles(articles)
        result = get_top_n_articles(articles, 3)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
