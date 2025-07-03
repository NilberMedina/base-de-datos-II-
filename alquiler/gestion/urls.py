from django.urls import path
from . import views


urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('registros/', views.lista_registros, name='lista_registros'),
    path('registro/agregar/', views.agregar_registro, name='agregar_registro'),
    path('registro/editar/<int:pk>/', views.editar_registro, name='editar_registro'),
    path('registro/eliminar/<int:pk>/', views.eliminar_registro, name='eliminar_registro'),
    path('cuartos/', views.lista_cuartos, name='lista_cuartos'),
    path('cuarto/agregar/', views.agregar_cuarto, name='agregar_cuarto'),
    path('cuarto/editar/<int:pk>/', views.editar_cuarto, name='editar_cuarto'),
    path('cuarto/eliminar/<int:pk>/', views.eliminar_cuarto, name='eliminar_cuarto'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamento/agregar/', views.agregar_departamento, name='agregar_departamento'),
    path('departamento/editar/<int:pk>/', views.editar_departamento, name='editar_departamento'),
    path('departamento/eliminar/<int:pk>/', views.eliminar_departamento, name='eliminar_departamento'),
]
