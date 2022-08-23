from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import BlogPost

# Create your views here.
class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published =True)
    
class blogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    