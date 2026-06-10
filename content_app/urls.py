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

router = DefaultRouter()
# Domínio de conteúdo / streaming
router.register(r'contents', ContentViewSet)
router.register(r'playlists', PlaylistViewSet, basename='playlist')
# Domínio de gestão de estágios
router.register(r'estudantes', EstudanteViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'professores', ProfessorOrientadorViewSet)
router.register(r'supervisores', SupervisorEmpresaViewSet)
router.register(r'estagios', EstagioViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = router.urls
