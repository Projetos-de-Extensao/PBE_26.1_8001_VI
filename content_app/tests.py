from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Content
from .serializers import ContentSerializer


class ContentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_content_creation(self):
        content = Content.objects.create(
            title='Test Video',
            description='Test Description',
            file_url='https://example.com/video.mp4',
            content_type='video',
            creator=self.user
        )
        self.assertEqual(content.title, 'Test Video')
        self.assertEqual(content.views, 0)
        self.assertEqual(content.likes, 0)
        self.assertTrue(content.is_public)
        self.assertEqual(content.status, 'published')
    
    def test_content_string_representation(self):
        content = Content.objects.create(
            title='Test Content',
            description='Test',
            file_url='https://example.com/file.mp4',
            content_type='video',
            creator=self.user
        )
        self.assertEqual(str(content), 'Test Content')
    
    def test_content_type_choices(self):
        content = Content.objects.create(
            title='Audio Content',
            description='Test',
            file_url='https://example.com/audio.mp3',
            content_type='audio',
            creator=self.user
        )
        self.assertIn(content.content_type, ['audio', 'video'])


class ContentSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_serializer_valid_data(self):
        data = {
            'title': 'New Video',
            'description': 'Description',
            'file_url': 'https://example.com/video.mp4',
            'content_type': 'video',
            'creator': self.user.id
        }
        serializer = ContentSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    
    def test_serializer_contains_expected_fields(self):
        content = Content.objects.create(
            title='Test',
            description='Test',
            file_url='https://example.com/video.mp4',
            content_type='video',
            creator=self.user
        )
        serializer = ContentSerializer(content)
        self.assertIn('id', serializer.data)
        self.assertIn('title', serializer.data)
        self.assertIn('creator', serializer.data)


class ContentAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.content = Content.objects.create(
            title='Test Video',
            description='Test',
            file_url='https://example.com/video.mp4',
            content_type='video',
            creator=self.user,
            is_public=True
        )
    
    def test_list_contents(self):
        response = self.client.get('/api/contents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_create_content_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Video',
            'description': 'New Description',
            'file_url': 'https://example.com/video2.mp4',
            'content_type': 'video'
        }
        response = self.client.post('/api/contents/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 2)
    
    def test_create_content_unauthenticated(self):
        data = {
            'title': 'New Video',
            'description': 'New Description',
            'file_url': 'https://example.com/video2.mp4',
            'content_type': 'video'
        }
        response = self.client.post('/api/contents/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
