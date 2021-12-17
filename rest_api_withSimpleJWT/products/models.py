from django.db import models

class Product(models.Model):
    name=models.CharField(verbose_name="Product Name",max_length=100, null=True, blank=True)
    price=models.PositiveIntegerField(default=0,null=True)
    stock_count=models.PositiveIntegerField(default=0,null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'



