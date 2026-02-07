from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name="Naziv")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="projects",
        verbose_name="Kategorija"
    )

    title = models.CharField(max_length=200, verbose_name="Naslov")
    slug = models.SlugField(unique=True)

    short_description = models.CharField(
        max_length=300, blank=True, verbose_name="Kratak opis")
    description = models.TextField(blank=True, verbose_name="Detaljan opis")

    bullets = models.TextField(
        blank=True,
        verbose_name="Šta je rađeno",
        help_text="Svaki red = jedna stavka (bullet)."
    )

    location = models.CharField(
        max_length=200, blank=True, verbose_name="Lokacija")
    duration = models.CharField(
        max_length=120, blank=True, verbose_name="Trajanje")
    price_from = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Cena od (RSD)")

    # ✅ BEZ Pillow: samo link ili /static/... putanja
    # primer: /static/img/krovovi/krov1.jpg  ili https://...
    cover_url = models.URLField(
        blank=True, verbose_name="Naslovna slika (URL ili /static/... putanja)")

    is_featured = models.BooleanField(default=False, verbose_name="Izdvojeno")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images")

    # ✅ BEZ Pillow: link ili /static/... putanja
    image_url = models.URLField(
        verbose_name="Slika (URL ili /static/... putanja)")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Opis")
    order = models.PositiveIntegerField(default=0, verbose_name="Redosled")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} ({self.order})"
