from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='project',null=False)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk +' : ' + self.title