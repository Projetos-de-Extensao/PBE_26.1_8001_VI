from django.contrib import admin
from .models import Content, Playlist, Estudante, Empresa, ProfessorOrientador, SupervisorEmpresa, Estagio, Relatorio


# Configuração da administração do modelo Content
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem do painel administrativo
    list_display = ('title', 'content_type', 'creator', 'upload_date', 'views', 'is_public', 'status')

    # Filtros disponíveis na lateral
    list_filter = ('content_type', 'is_public', 'status', 'upload_date')

    # Campos utilizados na busca
    search_fields = ('title', 'description', 'creator__username')

    # Campos que não podem ser editados manualmente
    readonly_fields = ('upload_date', 'views', 'likes')

    # Campos editáveis diretamente pela listagem
    list_editable = ('is_public', 'status')

    # Organização visual dos campos no painel
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'content_type', 'creator')
        }),
        ('URLs', {
            'fields': ('file_url', 'thumbnail_url')
        }),
        ('Metadados', {
            'fields': ('views', 'likes', 'is_public', 'status', 'upload_date'),
            'classes': ('collapse',)
        }),
    )

    # Impede alteração do criador após o conteúdo ser criado
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('creator',)
        return self.readonly_fields


# Configuração da administração do modelo Playlist
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')

    # Interface amigável para relacionamentos muitos-para-muitos
    filter_horizontal = ('contents',)


# Configuração da administração do modelo Estudante
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso')
    search_fields = ('nome', 'matricula', 'curso')


# Configuração da administração do modelo Empresa
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj')


# Configuração da administração do modelo ProfessorOrientador
@admin.register(ProfessorOrientador)
class ProfessorOrientadorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


# Configuração da administração do modelo SupervisorEmpresa
@admin.register(SupervisorEmpresa)
class SupervisorEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')
    search_fields = ('nome', 'empresa__nome')
    list_filter = ('empresa',)


# Configuração da administração do modelo Estagio
@admin.register(Estagio)
class EstagioAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'empresa', 'tipo', 'carga_horaria', 'status', 'professor_orientador', 'supervisor_empresa')
    list_filter = ('tipo', 'status', 'empresa')
    search_fields = ('estudante__nome', 'empresa__nome', 'professor_orientador__nome')

    # Permite alteração rápida do status pela listagem
    list_editable = ('status',)


# Configuração da administração do modelo Relatorio
@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('estagio', 'data_envio', 'status')
    list_filter = ('status', 'data_envio')
    search_fields = ('estagio__estudante__nome', 'estagio__empresa__nome')

    # Permite alteração rápida do status pela listagem
    list_editable = ('status',)