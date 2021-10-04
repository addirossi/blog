from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from main.forms import CreatePostForm
from main.models import Post


# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'main/posts_list.html', {'posts': posts})

class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_detail.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts-list')
