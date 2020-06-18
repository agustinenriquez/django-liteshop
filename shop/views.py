from .models import Item
from django.views.generic import ListView, DetailView


# Create your views here.
class ItemList(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item
