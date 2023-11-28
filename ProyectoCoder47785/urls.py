from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('AppCoder.urls')),
]

# Agrega tus propias rutas si es necesario
# urlpatterns += [path('otra/', include('otra_app.urls'))]
