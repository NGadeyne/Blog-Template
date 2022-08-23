from django.urls import path
from posts.apps import PostsConfig
from posts.models import BlogPost
from posts.views import BlogHome, blogPostDetail

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('<str:slug>/', blogPostDetail.as_view(), name="post")
]