from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now) # this is contengency
    # date_posted = models.DateTimeField(auto_now=True) # this sets the date to now every time it is updated
    # date_posted = models.DateTimeField(auto_now_add=True) # this sets the date to now the time it is created and we will not be able to change it later
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})