from django.shortcuts import render, redirect
from .models import Post
from .forms import UserForm, ArticleForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    Post_list = Post.objects.all().order_by('published_date')[:5]
    return render(request, 'blog/HTML/index.html', {'articles': Post_list})

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