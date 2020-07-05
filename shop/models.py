from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, unique=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=300, default=None, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True, unique=True, blank=True)
    items = models.ManyToManyField("Item", through="CartItem")
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    discount = models.CharField(default=None, max_length=8, null=True, blank=True)
    note = models.CharField(default=None, max_length=50, null=True)
    state = models.CharField(choices=(("OPEN", 1), ("CLOSED", 0)), default="OPEN", max_length=6)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

    def get_absolute_url(self):
        return reverse("cartitem-detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    coupon = models.CharField(max_length=50)
    last_purchase = models.ForeignKey("Item", on_delete=models.CASCADE, null=True)
    # card = models.ForeignKey("CreditCard", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
