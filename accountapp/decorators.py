from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        print(kwargs)
        if not user == request.user:
            print('request.uesr, user', request.user, user)
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated