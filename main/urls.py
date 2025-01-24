from django.urls import path

from .views import (
    index, product_details,
    shop, category,
    about, contacts
)

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("shop/<slug:category_slug>/<slug:product_slug>", product_details, name="product_details"),
    path("shop/<slug:category_slug>", category, name="category"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
]