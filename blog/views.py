from django.shortcuts import render, redirect
from .models import Post
import hashlib, string, random, time
# Create your views here.

def index(request):
    Post_list = Post.objects.all().order_by('published_date')[:5]
    return render(request, 'blog/HTML/index.html', {'articles': Post_list})

