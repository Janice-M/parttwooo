from django.shortcuts import render
from .models import Post

# Create your views here.

class PostList (generic.ListView):
    queryset = Post.object.filter(status=1).order_by('_created_on')
    template_name = 'index.html'