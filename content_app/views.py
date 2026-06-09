from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Content, Playlist
from .serializers import ContentSerializer, PlaylistSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.select_related('creator').all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['content_type', 'is_public', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['upload_date', 'views', 'likes']
    ordering = ['-upload_date']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def get_queryset(self):
        # Permite que o usuário veja apenas suas próprias playlists
        return Playlist.objects.prefetch_related('contents__creator').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
