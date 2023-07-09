from django.db import models
from django.contrib.auth.models import *
from froala_editor.fields import FroalaField
from .helpers import *
# Create your models here.



class Blogmodel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add = True)
    upload_to = models.DateTimeField(auto_now = True)


    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blogmodel, self).save(*args, **kwargs)

class Register(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=100)
    em = models.EmailField()
    password =models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name





