from .models import Item, CartItem, Cart, Profile
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ItemList(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item


class CartItemCreateView(CreateView):
    model = CartItem
    fields = "__all__"


class CartItemList(LoginRequiredMixin, ListView):
    model = CartItem
    login_url = "/users/add"

    def get_queryset(self):
        return super().get_queryset().filter(cart__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list.exists():
            cart_total = sum([item.item.price for item in self.object_list])
            self.object_list[0].cart.total = cart_total
            self.object_list[0].cart.save()
            context["cartitem_total"] = cart_total
            context["cart_id"] = self.object_list[0].cart.id
        else:
            context["cartitem_total"] = 0
        return context


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    success_url = "/"
    template_name = "web/create_user.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # Create profile with recently created User instance.
        Profile.objects.create(user=self.object)
        Cart.objects.create(user=self.object)
        login(self.request, self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


class SearchView(ListView):
    model = Item
    template_name = "shop/search_results.html"

    def get_queryset(self):
        search_box_query = self.request.GET["q"]
        return super().get_queryset().filter(name__contains=search_box_query)
