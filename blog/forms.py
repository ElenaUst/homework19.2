from django import forms
from blog.models import Blog
from catalog.forms import StyleMixin


class BlogForm(StyleMixin):

    class Meta:
        model = Blog
        exclude = ('slug', 'create_date', 'view_count',)
