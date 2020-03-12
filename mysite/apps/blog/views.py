from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'blog/post_list.html', {"posts" : posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'blog/post_create.html', {"posts" : posts})

def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "blog/post_create.html", context)