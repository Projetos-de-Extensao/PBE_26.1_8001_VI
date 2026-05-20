from django.contrib import admin
from .models import Content, Estudante, Empresa, ProfessorOrientador, SupervisorEmpresa, Estagio, Relatorio


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'creator', 'upload_date', 'views', 'is_public', 'status')
    list_filter = ('content_type', 'is_public', 'status', 'upload_date')
    search_fields = ('title', 'description', 'creator__username')
    readonly_fields = ('upload_date', 'views', 'likes')
    list_editable = ('is_public', 'status')
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
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('creator',)
        return self.readonly_fields


@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso')
    search_fields = ('nome', 'matricula', 'curso')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj')
    search_fields = ('nome', 'cnpj')


@admin.register(ProfessorOrientador)
class ProfessorOrientadorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(SupervisorEmpresa)
class SupervisorEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')
    search_fields = ('nome', 'empresa__nome')
    list_filter = ('empresa',)


@admin.register(Estagio)
class EstagioAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'empresa', 'tipo', 'carga_horaria', 'status', 'professor_orientador', 'supervisor_empresa')
    list_filter = ('tipo', 'status', 'empresa')
    search_fields = ('estudante__nome', 'empresa__nome', 'professor_orientador__nome')
    list_editable = ('status',)


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('estagio', 'data_envio', 'status')
    list_filter = ('status', 'data_envio')
    search_fields = ('estagio__estudante__nome', 'estagio__empresa__nome')
    list_editable = ('status',)
