from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by("created_date")
    return render(request, 'blog/post_list.html', {"posts" : posts})

def home(request):
    pops = Post.objects.all()
    return render(request, 'blog/base.html', {"posts" : pops})