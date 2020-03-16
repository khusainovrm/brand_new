from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path ('post/new/', views.post_new, name='post_new'),
    path ('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path ('post/<int:id>/comment', views.comment_new, name='add_comment'),
    path ('welcome/', views.welcome, name='welcome'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)