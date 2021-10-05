from django import forms
from django.contrib.auth.models import User


# class CreatePostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea)
#     user = forms.ModelChoiceField(queryset=User.objects.all())
#     image = forms.ImageField()
from main.models import Post


class CreatePostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        exclude = ('author', )

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.request.user
        post.save()
        return post


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', )
