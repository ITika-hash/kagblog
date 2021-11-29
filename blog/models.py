from django.db import models
from django.forms import ModelForm, TextInput, EmailInput

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

class About(models.Model):
    text = models.CharField(max_length=255)
    thumb = models.ImageField(default='default.png',blank=True)

    def save(self, *args, **kwargs):
        super(Model, self).save(*args, **kwargs)

class Tweet(models.Model):
    text = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(Model, self).save(*args, **kwargs)

class Insta(models.Model):
    text = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(Model, self).save(*args, **kwargs)
    
