from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('ver/', views.ver_empleados, name='ver_empleados'),  # ✅ OJO aquí con la “s”
    path('actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    # Clientes (nuevas rutas)
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_cliente, name='ver_cliente'),
    path('clientes/actualizar/<int:id_cli>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id_cli>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cli>/', views.borrar_cliente, name='borrar_cliente'),
    # ATRACCIONES
    path('atracciones/ver/', views.ver_atraccion, name='ver_atraccion'),
    path('atracciones/agregar/', views.agregar_atraccion, name='agregar_atraccion'),
    path('atracciones/actualizar/<int:id_atr>/', views.actualizar_atraccion, name='actualizar_atraccion'),
    path('atracciones/realizar_actualizacion/<int:id_atr>/', views.realizar_actualizacion_atraccion, name='realizar_actualizacion_atraccion'),
    path('atracciones/borrar/<int:id_atr>/', views.borrar_atraccion, name='borrar_atraccion'),
]
