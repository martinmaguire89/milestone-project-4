from django.db import models

""" This will display the products on the poduct page and database"""

PRODUCT_CHOICES = ([
        ('singles', 'singles'),
        ('mixed_cases', 'mixed_cases'),
        ('merchandise', 'merchandise'),
    ])


class Category(models.Model):
    name = models.CharField(max_length=120, choices=PRODUCT_CHOICES,
                            default='singles')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
