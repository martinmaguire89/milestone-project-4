from django.conf.urls import url, include
from .views import all_products, product_list

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^list$', product_list)
]
