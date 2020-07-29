from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.fred = Editor(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fred, Editor))
    
    #Testing save method
    def test_save_method(self):
        self.fred.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #create a new editor and save it
        self.fred = Editor(first_name='Fredrick', last_name='Ojure', email='fredojure@hotmail.com')
        self.fred.save_editor()

        #Create a new tag and save it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(title='Test Article', post='This is a random test Post', editor=self.fred)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)
    
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
    
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

