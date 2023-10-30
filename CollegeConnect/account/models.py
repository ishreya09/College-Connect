from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from branch.models import Department,Branch
from taggit.managers import TaggableManager
# Create your models here.

class Student(models.Model):
    student_id= models.CharField(primary_key=True,max_length=100,blank=False,null=False) # SRN
    bio= models.CharField(max_length=500,null=True, blank= True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True) # one to many
    college_email = models.EmailField(max_length=500,null=False,blank=False) # ends with @pesu.pes.edu
    whatsapp_number = models.CharField(null=True, blank=True, max_length=15) # for contact
    whatsapp_link=models.CharField(max_length=500,null=True,blank=True) # for connecting with mentors
    email_confirmed = models.BooleanField(default=False) # college email confirmed or not
    is_mentor= models.BooleanField(default=False)
    show_number=models.BooleanField(default=False) # choice for users to show their chat option
    year_of_passing_out= models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.user.username


class Mentor(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,related_name='mentor')
    username= models.CharField(max_length=300,blank=False,null=False,default="AnonymousUser")
    resume= models.FileField(upload_to='resume/')
    domain= TaggableManager()
    description= models.CharField(max_length=5000,null=True, blank= True)
    approved= models.BooleanField(default=False)

    # write list domains function which returns a string
    def list_domains(self):
        return ", ".join([p.name for p in self.domain.all()])
    

class Club(models.Model):
    club_name= models.CharField(max_length=200,unique=True)
    club_desc= models.CharField(max_length=200)
    club_id= models.BigAutoField(auto_created=True,primary_key=True)
    club_logo= models.ImageField(blank=True,null=True,upload_to='club_logo/')
    branch= models.ForeignKey(Branch,on_delete=models.CASCADE)
    def __str__(self):
        return self.club_name

class ClubMember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    club_head = models.BooleanField(default=False)
    social_media_manager= models.BooleanField(default=False)

