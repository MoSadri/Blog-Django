from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.creat_user(
        username = 'testuser',
        email = 'testemail.com',
        password = 'secret'
    )

        self.post = Post.objects.create(
        title = 'A good title',
        body = 'Nice body',
        author = self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

        
