from .models import Item, CartItem
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class ItemList(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item


class CartItemCreateView(CreateView):
    model = CartItem
    fields = "__all__"
