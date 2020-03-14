from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Список всех постов
def post_list(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'blog/post_list.html', {"posts" : posts})

#Детальное отображение выбранного поста
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

#Создание через форму нового поста
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# Редактирование через форму выбранный пост
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#Настройка комментариев
"""def create_comment(request):
    com = Comment.objects.all()"""

def comment_new(request, id):
    post = get_object_or_404 (Post, id=id)
    if request.method == "POST":
        form = CommentForm (request.POST)
        if form.is_valid ():
            comment = form.save (commit=False)
            comment.post = post
            comment.save ()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_new.html', {"form":form})