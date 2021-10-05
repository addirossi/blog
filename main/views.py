import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main.forms import CreatePostForm, UpdatePostForm
from main.models import Post


# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'main/posts_list.html', {'posts': posts})

class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'
    # paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        #2021-09-01
        date = self.request.GET.get('date')
        if date:
            # date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            queryset = queryset.filter(created_at__gt=date)
        return queryset


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_detail.html'
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# TODO: переиспользование шаблонов
# TODO: Делать автором request.user
# TODO: Permission (создавать может только залогиненный, изменять только автор)
# TODO: сделать верстку (через Bootstrap)
# TODO: сделать поиск, фильтрацию, пагинацию
class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_authenticated and\
               self.request.user == post.author


class UpdatePostView(IsAuthorMixin, UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/update_post.html'
    form_class = UpdatePostForm

    def get_success_url(self):
        post = self.get_object()
        return post.get_absolute_url()


class DeletePostView(IsAuthorMixin, DeleteView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts-list')


class SearchResultsView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) |
                                       Q(description__icontains=q))
        return queryset
