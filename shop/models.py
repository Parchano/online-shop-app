from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='PLN',
        max_digits=11,
        null=False,
        blank=False
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        null=True,
    )
    def __str__(self):
        return self.name
