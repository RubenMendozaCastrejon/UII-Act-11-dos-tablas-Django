from django.urls import path
from . import views

app_name = 'app_Usuario'

urlpatterns = [
    # URLs para Usuarios
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('usuario/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    
    # URLs para Portafolios
    path('usuario/<int:usuario_id>/crear-portafolio/', views.crear_portafolio, name='crear_portafolio'),
    path('portafolio/editar/<int:portafolio_id>/', views.editar_portafolio, name='editar_portafolio'),
    path('portafolio/borrar/<int:portafolio_id>/', views.borrar_portafolio, name='borrar_portafolio'),
]