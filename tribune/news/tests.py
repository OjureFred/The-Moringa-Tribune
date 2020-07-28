from django.test import TestCase
from .models import Editor, Article, tags

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
        self.assertTrue(len(editors) >0)

