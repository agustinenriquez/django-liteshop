from django.urls import path
from shop.views import ItemList, ItemDetailView, CartItemCreateView, CreateUser, CartItemList


urlpatterns = [
    path("", ItemList.as_view(), name="main-shop"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("cartitem/add/<int:pk>", CartItemCreateView.as_view(), name="cartitem-create"),
    path("cartitem/", CartItemList.as_view(), name="cartitem-list"),
    path("users/add", CreateUser.as_view(), name="add-user"),
]
