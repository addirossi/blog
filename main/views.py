from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

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


# TODO: Делать автором request.user
# TODO: Permission (создавать может только залогиненный, изменять только автор)
# TODO: сделать верстку (через Bootstrap)
# TODO: сделать поиск, фильтрацию, пагинацию


class UpdatePostView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/update_post.html'
    form_class = CreatePostForm

    def get_success_url(self):
        post = self.get_object()
        return post.get_absolute_url()


class DeletePostView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts-list')


