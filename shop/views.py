from .models import Item
from django.views.generic import ListView


# Create your views here.
class ItemList(ListView):
    model = Item
