from django.contrib import admin

from .models import Post
from .models import About
from .models import Tweet
from .models import Insta

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Tweet)
admin.site.register(Insta)