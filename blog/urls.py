from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_status, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_article/<int:post_id>', views.post_article, name='post_article'),

]