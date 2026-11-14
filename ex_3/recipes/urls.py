
from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.recipe_list, name="list"),
    path("<int:pk>/", views.recipe_detail, name="detail"),
    path("category/<str:name>/", views.category_detail, name="category"),
    path("search/", views.search, name="search"),
]
