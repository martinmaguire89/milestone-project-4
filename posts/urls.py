from django.conf.urls import url
from .views import get_posts, create_or_edit_post, post_detail

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?p<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]
