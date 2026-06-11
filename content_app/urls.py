from rest_framework.routers import DefaultRouter

from .views import (
    ContentViewSet,
    EmpresaViewSet,
    EstagioViewSet,
    EstudanteViewSet,
    PlaylistViewSet,
    ProfessorOrientadorViewSet,
    RelatorioViewSet,
    SupervisorEmpresaViewSet,
)

# Instância principal do roteador da API
router = DefaultRouter()

# Rotas relacionadas ao domínio de conteúdo e streaming
router.register(r'contents', ContentViewSet)
router.register(r'playlists', PlaylistViewSet, basename='playlist')

# Rotas relacionadas ao domínio de gestão de estágios
router.register(r'estudantes', EstudanteViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'professores', ProfessorOrientadorViewSet)
router.register(r'supervisores', SupervisorEmpresaViewSet)
router.register(r'estagios', EstagioViewSet)
router.register(r'relatorios', RelatorioViewSet)

# Lista final de URLs geradas automaticamente pelo DRF
urlpatterns = router.urls