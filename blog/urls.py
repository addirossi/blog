"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import PostsListView, PostDetailsView, CreatePostView, UpdatePostView, DeletePostView, SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostsListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', PostDetailsView.as_view(), name='post-detail'),
    path('posts/create/', CreatePostView.as_view(), name='create-post'),
    path('posts/update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('posts/delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('posts/search/', SearchResultsView.as_view(), name='search-results')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
