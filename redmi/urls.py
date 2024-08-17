from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    index,
    list_view,
    details_view
)

urlpatterns = [
    path('', list_view, name='list_view'),
    path('details/<int:id>', details_view, name='details_view'),
    path('index/', index, name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)