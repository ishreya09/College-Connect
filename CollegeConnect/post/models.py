from django.db import models
import django.utils.timezone


from mptt.models import MPTTModel, TreeForeignKey
from mptt.models import TreeManyToManyField

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from branch.models import *


from django.utils import timezone
from django.db.models import Q


# Create your models here.

class Post(models.Model):
    user=  models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True,auto_created=True)
    content= RichTextUploadingField(blank=True,null=True)
    author= models.CharField(max_length=500,default="Anonymous")
    branch = models.ManyToManyField(Branch,verbose_name='branches')
    tags=TaggableManager()
    created_at=models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.title

class PostComment(models.Model):
    comment_id= models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    comment= models.CharField(max_length=5000, blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    post= models.ForeignKey(Post,on_delete=models.CASCADE)