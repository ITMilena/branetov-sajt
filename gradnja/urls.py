from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("galerija/", views.gallery, name="gallery"),
    path("ponuda/", views.ponuda, name="ponuda"),
    path("o-nama/", views.onama, name="onama"),
    path("kontakt/", views.kontakt, name="kontakt"),

    path("kategorija/<slug:slug>/", views.category_detail, name="category_detail"),
    path("projekat/<slug:slug>/", views.project_detail, name="project_detail"),
]
