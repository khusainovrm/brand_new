from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path ('', views.post_list, name='main_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail_name'),
    path('create/', views.post_create_view, name ='create'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)