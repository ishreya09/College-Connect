from django.db import models
from multiupload.fields import MultiFileField
from taggit.managers import TaggableManager
from branch.models import Branch

def upload_to(instance, filename):
    return 'resources/{}/{}'.format(instance.branch.branch_name, filename)

class UploadedFile(models.Model):
    title = models.CharField(max_length=255)
    files = MultiFileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='uploaded_files', null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title