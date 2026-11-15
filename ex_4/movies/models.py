from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):

    class AgeRating(models.TextChoices):
        G = "G", "yvelastvis"
        PG = "PG", "mshoblis tanxlebit"
        PG13 = "PG13", "13+"
        R = "R", "18+"
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    language = models.CharField(max_length=30, default="qartuli")

    age_rating = models.CharField(max_length=4, choices=AgeRating.choices, default=AgeRating.G)
    
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-release_year"]
        verbose_name = "filmi"
        verbose_name_plural = "filmebi"

    def __str__(self):
        return f"{self.title} ({self.release_year})"