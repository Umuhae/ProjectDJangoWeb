from django.forms import ModelForm
from .models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["image", 'nickname', 'message']
        labels = {
            'image': '썸네일 변경',
            'nickname': '닉네임 변경',
            'message': '자기소개 변경',
        }