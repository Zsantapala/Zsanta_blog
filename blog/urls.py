from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_status, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post_article/<int:post_id>', views.post_article, name='post_article'),
    path('edit_post/<int:post_id>', views.Edit_Post, name='edit_post'),
    path('new_post/', views.new_post, name='new_post'),
    path('p/', views.post_list, name='p')
]