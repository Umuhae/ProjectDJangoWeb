from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project','content']

        widgets = {
            'content': SummernoteWidget(),
        }