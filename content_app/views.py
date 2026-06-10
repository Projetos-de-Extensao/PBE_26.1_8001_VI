from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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
from .serializers import (
    ContentSerializer,
    EmpresaSerializer,
    EstagioSerializer,
    EstudanteSerializer,
    PlaylistSerializer,
    ProfessorOrientadorSerializer,
    RelatorioSerializer,
    SupervisorEmpresaSerializer,
)


class ContentViewSet(viewsets.ModelViewSet):
    # select_related evita N+1 ao serializar o criador.
    queryset = Content.objects.select_related('creator').all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['content_type', 'is_public', 'status', 'creator']
    search_fields = ['title', 'description']
    ordering_fields = ['upload_date', 'views', 'likes', 'title']
    ordering = ['-upload_date']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        # Incrementa likes de forma controlada (campo é read-only no serializer).
        content = self.get_object()
        Content.objects.filter(pk=content.pk).update(likes=content.likes + 1)
        content.refresh_from_db()
        return Response({'id': content.id, 'likes': content.likes})

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        # Incrementa a contagem de visualizações.
        content = self.get_object()
        Content.objects.filter(pk=content.pk).update(views=content.views + 1)
        content.refresh_from_db()
        return Response({'id': content.id, 'views': content.views})


class PlaylistViewSet(viewsets.ModelViewSet):
    # prefetch_related evita N+1 ao aninhar os conteúdos e seus criadores.
    queryset = Playlist.objects.prefetch_related('contents__creator').all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'title']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Permite que o usuário veja apenas suas próprias playlists.
        return super().get_queryset().filter(user=self.request.user)


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['curso']
    search_fields = ['nome', 'matricula', 'curso']
    ordering_fields = ['nome', 'matricula']


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome', 'cnpj']
    ordering_fields = ['nome']


class ProfessorOrientadorViewSet(viewsets.ModelViewSet):
    queryset = ProfessorOrientador.objects.all()
    serializer_class = ProfessorOrientadorSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
    ordering_fields = ['nome']


class SupervisorEmpresaViewSet(viewsets.ModelViewSet):
    queryset = SupervisorEmpresa.objects.select_related('empresa').all()
    serializer_class = SupervisorEmpresaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['empresa']
    search_fields = ['nome', 'empresa__nome']
    ordering_fields = ['nome']


class EstagioViewSet(viewsets.ModelViewSet):
    queryset = Estagio.objects.select_related(
        'estudante', 'empresa', 'professor_orientador', 'supervisor_empresa'
    ).all()
    serializer_class = EstagioSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['tipo', 'status', 'empresa', 'estudante', 'professor_orientador']
    search_fields = ['estudante__nome', 'empresa__nome', 'professor_orientador__nome']
    ordering_fields = ['carga_horaria', 'status']


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.select_related('estagio__estudante', 'estagio__empresa').all()
    serializer_class = RelatorioSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'estagio']
    search_fields = ['estagio__estudante__nome', 'estagio__empresa__nome']
    ordering_fields = ['data_envio', 'status']
