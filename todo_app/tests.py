from django.test import TestCase, Client, override_settings
from django.urls import reverse
from .models import Todo

# Create your tests here.

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_todo_url = reverse('todos:create_todo')
        self.todo_list_url = reverse('todos:todo_list')

    def test_create_todo_POST(self):
        response = self.client.post(self.create_todo_url, {
            'title': 'Test Todo',
            'completed': False
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test Todo')

    def test_todo_list_GET(self):
        response = self.client.get(self.todo_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list.html')
