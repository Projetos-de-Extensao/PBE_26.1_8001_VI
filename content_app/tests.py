from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import (
    Content,
    Empresa,
    Estagio,
    Estudante,
    Playlist,
    ProfessorOrientador,
    Relatorio,
    SupervisorEmpresa,
)
from .serializers import ContentSerializer

API = '/api/v1'


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
        }
        serializer = ContentSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

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

    def test_views_and_likes_are_read_only(self):
        # NC-09: cliente não deve conseguir gravar views/likes.
        self.assertIn('views', ContentSerializer.Meta.read_only_fields)
        self.assertIn('likes', ContentSerializer.Meta.read_only_fields)


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
        response = self.client.get(f'{API}/contents/')
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
        response = self.client.post(f'{API}/contents/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 2)

    def test_create_content_unauthenticated(self):
        # NC-17: com JWTAuthentication, requisições sem credenciais retornam 401.
        data = {
            'title': 'New Video',
            'description': 'New Description',
            'file_url': 'https://example.com/video2.mp4',
            'content_type': 'video'
        }
        response = self.client.post(f'{API}/contents/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creator_set_automatically(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Owned',
            'description': 'x',
            'file_url': 'https://example.com/v.mp4',
            'content_type': 'video',
        }
        response = self.client.post(f'{API}/contents/', data, format='json')
        self.assertEqual(Content.objects.get(title='Owned').creator, self.user)

    def test_views_not_writable_by_client(self):
        # Mesmo enviando views, o valor não deve ser alterado pelo cliente.
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f'{API}/contents/{self.content.id}/', {'views': 999999}, format='json'
        )
        self.content.refresh_from_db()
        self.assertEqual(self.content.views, 0)

    def test_like_action_increments(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(f'{API}/contents/{self.content.id}/like/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.content.refresh_from_db()
        self.assertEqual(self.content.likes, 1)


class PlaylistAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='owner', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')
        self.content = Content.objects.create(
            title='C1', description='d', file_url='https://e.com/a.mp4',
            content_type='audio', creator=self.user
        )

    def test_create_playlist_sets_user(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Minha', 'description': 'x', 'content_ids': [self.content.id]}
        response = self.client.post(f'{API}/playlists/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.get().user, self.user)

    def test_user_only_sees_own_playlists(self):
        Playlist.objects.create(title='Do dono', user=self.user)
        Playlist.objects.create(title='Do outro', user=self.other)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'{API}/playlists/')
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Do dono')

    def test_playlist_requires_authentication(self):
        response = self.client.get(f'{API}/playlists/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EstagioAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='coord', password='pass12345')
        self.estudante = Estudante.objects.create(nome='Ana', matricula='2026001', curso='ADS')
        self.empresa = Empresa.objects.create(nome='ACME', cnpj='12.345.678/0001-90')
        self.professor = ProfessorOrientador.objects.create(nome='Prof. Silva')
        self.supervisor = SupervisorEmpresa.objects.create(nome='Sup. João', empresa=self.empresa)

    def test_create_estagio(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'tipo': 'obrigatorio',
            'carga_horaria': 300,
            'estudante': self.estudante.id,
            'empresa': self.empresa.id,
            'professor_orientador': self.professor.id,
            'supervisor_empresa': self.supervisor.id,
        }
        response = self.client.post(f'{API}/estagios/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Estagio.objects.count(), 1)

    def test_carga_horaria_must_be_positive(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'tipo': 'obrigatorio',
            'carga_horaria': 0,
            'estudante': self.estudante.id,
            'empresa': self.empresa.id,
            'professor_orientador': self.professor.id,
            'supervisor_empresa': self.supervisor.id,
        }
        response = self.client.post(f'{API}/estagios/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_supervisor_must_belong_to_empresa(self):
        outra_empresa = Empresa.objects.create(nome='Outra', cnpj='98.765.432/0001-10')
        outro_supervisor = SupervisorEmpresa.objects.create(nome='Externo', empresa=outra_empresa)
        self.client.force_authenticate(user=self.user)
        data = {
            'tipo': 'obrigatorio',
            'carga_horaria': 100,
            'estudante': self.estudante.id,
            'empresa': self.empresa.id,
            'professor_orientador': self.professor.id,
            'supervisor_empresa': outro_supervisor.id,
        }
        response = self.client.post(f'{API}/estagios/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estagio_requires_authentication(self):
        response = self.client.get(f'{API}/estagios/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RelatorioAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='coord', password='pass12345')
        estudante = Estudante.objects.create(nome='Bia', matricula='2026002', curso='SI')
        empresa = Empresa.objects.create(nome='Globex', cnpj='11.222.333/0001-44')
        professor = ProfessorOrientador.objects.create(nome='Prof. Souza')
        supervisor = SupervisorEmpresa.objects.create(nome='Sup', empresa=empresa)
        self.estagio = Estagio.objects.create(
            tipo='nao_obrigatorio', carga_horaria=200, estudante=estudante,
            empresa=empresa, professor_orientador=professor, supervisor_empresa=supervisor,
        )

    def test_create_and_default_status(self):
        self.client.force_authenticate(user=self.user)
        data = {'data_envio': '2026-06-01', 'estagio': self.estagio.id}
        response = self.client.post(f'{API}/relatorios/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Relatorio.objects.get().status, 'pendente')

    def test_filter_by_status(self):
        Relatorio.objects.create(data_envio='2026-06-01', status='aprovado', estagio=self.estagio)
        Relatorio.objects.create(data_envio='2026-06-02', status='pendente', estagio=self.estagio)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'{API}/relatorios/?status=aprovado')
        self.assertEqual(response.data['count'], 1)
