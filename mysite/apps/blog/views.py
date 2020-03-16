from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView



#Список всех постов
class PostListView(ListView):
    context_object_name = "posts"
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.order_by("-created_date")

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

#Создание через форму нового поста
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# Редактирование через форму выбранный пост
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def comment_new(request, pk):
    post = get_object_or_404 (Post, pk=pk)
    if request.method == "POST":
        form = CommentForm (request.POST)
        if form.is_valid ():
            comment = form.save (commit=False)
            comment.post = post
            comment.author = request.user
            comment.save ()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_new.html', {"form":form})

def welcome(request):
    return render(request, 'blog/welcome.html')

def new_search(request):
    search = request.POST.get('search')
    return render(request, 'blog/new_search.html', {'search': search})
