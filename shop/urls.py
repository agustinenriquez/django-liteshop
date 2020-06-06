from django.urls import path
from shop.views import ItemList


urlpatterns = [
        path("", ItemList.as_view(), name="main-shop"),
]
