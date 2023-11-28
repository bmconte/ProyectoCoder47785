from django.urls import path
from AppCoder.views import CursoEliminar, CursoActualizacion, CursoCreacion, CursoDetalle, crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada, CursoList

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
    path('cursos/listar', CursoList.as_view(), name="CursosList"),
    path('curso/<int:pk>', CursoDetalle.as_view(), name="CursoDetail"),
    path('crear', CursoCreacion.as_view(), name="CursoCreate"),
    path('editar/<int:pk>', CursoActualizacion.as_view(), name="CursoEditar"),
    path('eliminar/<int:pk>', CursoEliminar.as_view(), name="CursoEliminar"),
]
