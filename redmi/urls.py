from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    index,
    Redmi_list_view,
    Redmi_details_view,
    Redmi_create_view,
    Redmi_delete_view,
    Redmi_update_view,
    post_detail,
    # signup,
    # login,
    # login_required,




)

urlpatterns = [
    path('list_view/', Redmi_list_view.as_view(), name='list_view'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('details/<int:id>/', Redmi_details_view.as_view(), name='details_view'),
    path('index/', index, name='index'),
    path('create/', Redmi_create_view.as_view(), name='create_phone_view'),
    path('delete/<int:id>/', Redmi_delete_view.as_view(), name='delete_phone_view'),
    path('update/<int:id>/', Redmi_update_view.as_view(), name='update_phone_view')
    # path('signup/', signup, name='signup'),
    # path('login/', login, name='login'),
    # path('login_required/', login_required, name='some_view'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)