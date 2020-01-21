from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE) #on_delete=models.CASCADE is used for "When we delete a user, all posts that was posted by that user"

    def __str__(self):
        return self.title

    def  get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) 


