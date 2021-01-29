from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']
        labels = {
            'title': '게시판 제목',
            'image': '게시판 대표이미지',
            'description': '게시판 설명',
        }