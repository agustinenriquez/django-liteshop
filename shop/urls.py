from django.urls import path
from shop.views import ItemList, ItemDetailView


urlpatterns = [
        path("", ItemList.as_view(), name="main-shop"),
        path("/item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
]
