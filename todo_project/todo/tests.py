from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='The good life', body='Something else')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'The good life')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        result = 'Something else'
        self.assertEquals(todo.body, result)
    

