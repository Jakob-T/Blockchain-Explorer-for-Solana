from django.urls import path
from .views import home, tx_detail, account_detail, search, slot_detail

urlpatterns = [
    path("", home, name="home"),
    path("search", search, name="search"),
    path("slot/<int:slot>/", slot_detail, name="slot_detail"),
    path("tx/<str:signature>/", tx_detail, name="tx_detail"),
    path("account/<str:address>/", account_detail, name="account_detail"),
]