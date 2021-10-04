from django import forms
from django.contrib.auth.models import User


# class CreatePostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea)
#     user = forms.ModelChoiceField(queryset=User.objects.all())
#     image = forms.ImageField()
from main.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
