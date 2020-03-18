from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    #path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path ('post/new/', views.post_new, name='post_new'),
    path ('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path ('post/<int:pk>/comment/', views.comment_new, name='add_comment'),
    path ('welcome/', views.welcome, name='welcome'),
    path ('search/', views.new_search, name='new_search'),
    path ('banklist/', views.bank_list, name = 'bank_list'),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)