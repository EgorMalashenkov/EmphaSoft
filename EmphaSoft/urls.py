from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # djoser paths endpoints
    path('auth/', include('djoser.urls.jwt')),

    # Users app endpoints path
    path('api/v1/', include('Users.urls')),



]
urlpatterns += doc_urlpatterns
