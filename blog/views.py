from django.shortcuts import render, redirect
from .models import Post
from .forms import UserForm, PostForm
from django.contrib.auth import authenticate, login, logout   #导入认证模块
from django.contrib.auth.models import User                   #导入认证用户模块
from django.core.paginator import Paginator                   #导入分页功能模块
from django.utils import timezone
# Create your views here.

def index(request):
    Post_list = Post.objects.all().order_by('created_date')[:5]
    return render(request, 'blog/HTML/index.html', {'posts': Post_list})

def login_status(request):
    if request.session.get('is_login', None):
        return redirect('index')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                login(request, user)
                return redirect('index')
            else:
                message = '用户不存在或密码错误！'
                return render(request, 'blog/HTML/login.html', {'message': message, 'login_form': login_form})
    login_form = UserForm
    return render(request, 'blog/HTML/login.html', locals())

def logout_view(request):
    if not request.session.get('is_login', None):
        return redirect('index')
    logout(request)
    return redirect('index')

def post_article(request, post_id):
    post = Post.objects.get(pk=post_id)
    edit_status = False
    if request.session.get('is_login', None):
        username = request.session.get('user_name', None)
        if username == post.author.username:
            edit_status = True
            return render(request, 'blog/HTML/post_article.html', {'post': post, 'edit_status': edit_status})
    return render(request, 'blog/HTML/post_article.html', {'post': post, 'edit_status': edit_status})

def Edit_Post(request,post_id):
    if not request.session.get('is_login', None):
        return redirect('index')
    user = User.objects.get(username=request.session.get('user_name', None))
    post = Post.objects.get(pk=post_id)
    new_post = False
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.publish()
        return redirect('index')
    elif post.author == user:
        post_info = {
            'title': post.title,
            'text': post.text,
        }
        post_form = PostForm(initial=post_info)
        return render(request, 'blog/HTML/edit_post.html', {'postform': post_form, 'post': post, 'new_post': new_post})
    return redirect('index')

def new_post(request):
    if not request.session.get('is_login', None):
        return redirect('index')
    user = User.objects.get(username=request.session.get('user_name', None))
    new_post = True
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        message = "请输入标题和内容！"
        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            text = post_form.cleaned_data['text']
            post = Post.objects.create(author=user, title=title, text=text)
            post.publish()
            return redirect('index')
        else:
            return render(request, 'blog/HTML/edit_post.html', {'message': message, 'new_post': new_post})
    postform = PostForm()
    return render(request, 'blog/HTML/edit_post.html', {'new_post': new_post, 'postform': postform})

def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    page_info = Paginator(post_list, 2)

    page = request.GET.get('page')
    contents = page_info.get_page(page)
    return render(request, 'blog/HTML/post_list.html', {'contents': contents})
