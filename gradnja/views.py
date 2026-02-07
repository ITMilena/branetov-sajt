from django.shortcuts import render, get_object_or_404
from .models import Category, Project


def home(request):
    categories = Category.objects.all().order_by("name")
    featured = Project.objects.filter(is_featured=True).order_by("-id")[:6]
    return render(request, "home.html", {"categories": categories, "featured": featured})


def gallery(request):
    projects = Project.objects.prefetch_related("images").order_by("-id")
    return render(request, "gallery.html", {"projects": projects})


def ponuda(request):
    return render(request, "ponuda.html")


def onama(request):
    return render(request, "onama.html")


def kontakt(request):
    return render(request, "kontakt.html")


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    projects = Project.objects.filter(
        category=category).prefetch_related("images").order_by("-id")
    return render(request, "category.html", {"category": category, "projects": projects})


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.prefetch_related("images"), slug=slug)

    bullets = []
    if getattr(project, "bullets", ""):
        bullets = [x.strip()
                   for x in project.bullets.splitlines() if x.strip()]

    return render(request, "project.html", {"project": project, "bullets": bullets})
