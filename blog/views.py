from django.shortcuts import render
from django.views.generic import ListView , DetailView
from blog.models import Post
# Create your views here.



class blogListView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'mera_blog'

class detailBlogView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = "mera_post_blog"
