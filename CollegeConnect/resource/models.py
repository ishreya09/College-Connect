from django.db import models
from taggit.managers import TaggableManager
from branch.models import Branch

class Resource(models.Model):
    title = models.CharField(max_length=255)
    files = models.FileField(upload_to='resource/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch', null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title