from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.nexus_home,name='nexus_home'),
    url(r'^post/new/$',views.post_new, name='post_new')
]