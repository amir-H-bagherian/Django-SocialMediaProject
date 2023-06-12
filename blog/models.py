from django.db import models
from django.contrib.auth.models import User, AnonymousUser


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_DEFAULT,
                               default=AnonymousUser, related_name='posts'
                               )
    is_available = models.BooleanField(default=True)
    is_important = models.BooleanField(default=True)
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post,
                             on_delete=models.CASCADE,
                             related_name='comments'
                             )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    