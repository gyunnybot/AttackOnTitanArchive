from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='projects')  # 추가돼 있어야 함

    def __str__(self):
        return f"{self.pk} : {self.name}"