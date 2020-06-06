from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, unique=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=300, default=None, null=True)

    def __str__(self):
        return self.name
