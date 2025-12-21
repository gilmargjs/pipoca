
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pipoca.views import pipoca_view, new_pipoca_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pipoca/', pipoca_view, name='pipoca_list'),
    path('new_pipoca/', new_pipoca_view, name='new_pipoca'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
