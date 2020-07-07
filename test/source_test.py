import unittest
from app.models import source,article

Articles = article.Articles
Sources = source.Sources

class ArticleTest(unittest.TestCase):
    """
    Test Class to test behaviour of source class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('','','','','','','')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))



class SourceTest(unittest.TestCase):
    """
    Test Class to test behaviour of source class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('','','','','','')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))   


if __name__ == '__main__':
    unittest.main()