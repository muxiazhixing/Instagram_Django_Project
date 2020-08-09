"""Insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Insta.views import  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserDetailView
from Insta.views import addLike, addComment, SignUp, HelloWorld, EditProfile, ExploreView


urlpatterns = [
    path('helloworld/', HelloWorld.as_view(), name='helloworld'),
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('user_profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('explore', ExploreView.as_view(), name='explore'),
]
