from django import forms
from .models import Post


class ImgForm(forms.ModelForm):
    model = Post
    fields = ['image']
