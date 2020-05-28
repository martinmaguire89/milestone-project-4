from django.conf.urls import url, include
from .views import all_products, cases

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^cases/$', cases, name='cases'),
]
