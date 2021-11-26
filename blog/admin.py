from django.contrib import admin

from .models import Post

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Tweet)
admin.site.register(Insta)