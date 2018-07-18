from __future__ import unicode_literals
from django.db import models



class Product(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    creaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return '< name item: {} Prices {}>'.format(self.item, self.price)