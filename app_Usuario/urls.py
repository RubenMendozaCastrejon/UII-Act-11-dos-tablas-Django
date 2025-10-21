from django.urls import path
from . import views

app_name = 'app_Usuario' # Cambiado a 'app_Usuario'

urlpatterns = [
    # URLs para el modelo Usuario
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),

    # URLs para el modelo Portafolio
    path('', views.listar_portafolios, name='listar_portafolios'),
    path('portafolios/<int:portafolio_id>/', views.detalle_portafolio, name='detalle_portafolio'),
    path('portafolios/crear/', views.crear_portafolio, name='crear_portafolio'),
    path('portafolios/editar/<int:portafolio_id>/', views.editar_portafolio, name='editar_portafolio'),
    path('portafolios/borrar/<int:portafolio_id>/', views.borrar_portafolio, name='borrar_portafolio'),
]