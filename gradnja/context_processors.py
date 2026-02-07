from .models import Category


def nav_categories(request):
    return {"categories_nav": Category.objects.all()}
