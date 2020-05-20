from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
