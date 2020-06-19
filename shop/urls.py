from django.urls import path
from shop.views import ItemList, ItemDetailView, CartItemCreateView


urlpatterns = [
        path("", ItemList.as_view(), name="main-shop"),
        path("/item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
        path("cartitem/add/<int:pk>", CartItemCreateView.as_view(), name="cartitem-create"),
]
