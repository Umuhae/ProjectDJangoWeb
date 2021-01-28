from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import  Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Comment.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated