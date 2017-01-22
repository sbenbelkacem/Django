from django.conf.urls import include, url
from django.contrib import admin
from  .  import views  

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[1-9]+)$', views.detail, name='detail'),
    url(r'^update_email$', views.update_email, name='update_email'),
    # url(r'^blog/', include('blog.urls')),
]
