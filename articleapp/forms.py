from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article

class ArticleCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True


    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        labels = {
            'project': '게시판',
        }
        widgets = {
            'content': SummernoteWidget(),
        }
