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
    slug = models.SlugField(unique=True)
    content= RichTextUploadingField(blank=True,null=True)
    author= models.CharField(max_length=500,default="anonymous")
    published_date= models.DateField(auto_now_add=True,blank=True,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name='branches')
    tags=TaggableManager()
    created_at=models.DateTimeField(auto_now_add=True)
    featured_img= models.ImageField(blank=True,null=True,upload_to='post/')
    
    def __str__(self):
        return self.title

class PostComment(models.Model):
    comment_id= models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    comment= models.CharField(max_length=5000, blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    post= models.ForeignKey(Post,on_delete=models.CASCADE)