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

class About(admin.ModelAdmin):
    text = models.CharField(max_length=255)
    thumb = models.ImageField(default='default.png',blank=True)

    ModelAdmin.save_model(self, request, obj, form, change)

class Tweet(admin.ModelAdmin):
    text = models.CharField(max_length=255)

    ModelAdmin.save_model(self, request, obj, form, change)

class Insta(models.Model):
    text = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(Insta, self).save(*args, **kwargs)
    
