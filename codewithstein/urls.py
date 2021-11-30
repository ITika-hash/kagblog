from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from blog.views import frontpage, post_detail, base

urlpatterns = [
    path('', base, name='base'),
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

]
urlpatterns += [
    path(r'^front-edit/', include('front.urls')),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
