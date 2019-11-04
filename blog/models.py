from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200)
    author = models.CharField(max_length = 200)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    status = models.IntegerField(choices = STATUS, default = 0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
