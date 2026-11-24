from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Genre(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Director(TimeStampedModel):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Movie(TimeStampedModel):

    class AgeRating(models.TextChoices):
        G = "G", "yvelastvis"
        PG = "PG", "mshoblis tanxlebit"
        PG13 = "PG13", "13+"
        R = "R", "18+"
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies",)
    cast = models.ManyToManyField("Actor", through="Role", related_name="movies")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    language = models.CharField(max_length=30, default="qartuli")
    age_rating = models.CharField(max_length=4, choices=AgeRating.choices, default=AgeRating.G)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-release_year"]
        verbose_name = "filmi"
        verbose_name_plural = "filmebi"

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class BoxOffice(TimeStampedModel):
    movie =models.OneToOneField(Movie, on_delete=models.CASCADE, related_name="box_office")
    tickets_sold = models.PositiveIntegerField()
    gross = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title}: salaro"

class Actor(TimeStampedModel):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")
    actor =models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    character_name = models.CharField(max_length=100)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["movie", "actor", "character_name"], name="unique_actor_movie_character",)]

    def __str__(self):
        return f"{self.actor.name} - {self.character_name}"