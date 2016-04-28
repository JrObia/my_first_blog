from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True,null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title   

