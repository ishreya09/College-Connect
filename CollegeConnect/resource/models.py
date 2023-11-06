from django.db import models
from taggit.managers import TaggableManager
from branch.models import Branch
from django.contrib.auth.models import User

class Resource(models.Model):
    # pk
    id = models.AutoField(primary_key=True,auto_created=True)
    user=  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=255)
    files = models.FileField(upload_to='resource/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    branch = models.ManyToManyField(Branch, related_name='branch')
    tags = TaggableManager()

    def __str__(self):
        return self.title