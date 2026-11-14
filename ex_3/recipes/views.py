from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, Http404

RECIPES = [
    {"id": 1, "slug": "khinkali", "name": "ხინკალი", "category": "main",
     "minutes": 90, "vegetarian": False,
     "ingredients": ["ფქვილი", "საქონლის ხორცი", "ღორის ხორცი",
                     "ხახვი", "კვლიავი"]},
    {"id": 2, "slug": "khachapuri", "name": "ხაჭაპური", "category":
     "bakery", "minutes": 60, "vegetarian": True,
     "ingredients": ["ფქვილი", "იმერული ყველი", "კვერცხი", "კარაქი"]},
    {"id": 3, "slug": "lobiani", "name": "ლობიანი", "category": "bakery",
     "minutes": 75, "vegetarian": True,
     "ingredients": ["ფქვილი", "ლობიო", "ხახვი", "კარაქი"]},
    {"id": 4, "slug": "pkhali", "name": "ფხალი", "category": "snack",
     "minutes": 30, "vegetarian": True,
     "ingredients": ["ისპანახი", "ნიგოზი", "ნიორი", "ქინძი"]},
    {"id": 5, "slug": "churchkhela", "name": "ჩურჩხელა", "category": "dessert", "minutes": 240, "vegetarian": True,
     "ingredients": ["ნიგოზი", "ყურძნის წვენი", "ფქვილი"]},
    {"id": 6, "slug": "chakapuli", "name": "ჩაქაფული", "category":
     "main", "minutes": 120, "vegetarian": False,
     "ingredients": ["ცხვრის ხორცი", "ტყემალი", "ტარხუნა", "თეთრი ღვინო"]},
]


def page(title, body):
    """ყველა გვერდისთვის ერთნაირი HTML ჩარჩო."""
    return HttpResponse(f"<h1>{title}</h1>{body}<hr><a href='/recipes/'>← ყველა რეცეპტი</a>")

def recipe_list(request):
    recipes = RECIPES

    category = request.GET.get("category")
    max_time = request.GET.get("max_time")
    vegetarian = request.GET.get("vegetarian")

    if category:
        recipes = [
            recipe for recipe in recipes
            if recipe["category"] == category
        ]

    if max_time:
        recipes = [
            recipe for recipe in recipes
            if recipe["minutes"] <= int (max_time)
        ]

    if vegetarian == "yes":
        recipes = [
            recipe for recipe in recipes
            if recipe["vegetarian"] is True
        ]
    
    items = "".join(
        f"<li><a href='/recipes/{recipe['id']}/'>{recipe['name']}</a> - {recipe['minutes']} wuti</li>"
        for recipe in recipes
    )

    return page("yvela recepti", f"<ul>{items}</ul>")

def find_recipe(pk):
    return next((recipe for recipe in RECIPES if recipe["id"] == pk), None)

def recipe_detail(request, pk):
    recipe = find_recipe(pk)

    if recipe is None:
        raise Http404("recepti ver moidzebna")

    ingredients = "".join(
        f"<li>{ingredient}</li>"
        for ingredient in recipe["ingredients"]
    )

    body = (
        f"<p>momzadebis dro: {recipe['minutes']} wuti</p>"
        f"<p>kategoria: {recipe['category']}</p>"
        f"<p>vegeterianulia: {'diax' if recipe['vegetarian'] else 'ara'}</p>"
        f"<h2>ingredientebi:</h2><ul>{ingredients}</ul>"
    
    )

    return page(recipe["name"], body)


def category_detail(request, name):
    recipes = [
        recipe for recipe in RECIPES
        if recipe["category"] == name
    ]

    if not recipes:
        raise Http404("kategoria ver moidzebna")

    items = "".join(
        f"<li><a href='/recipes/{recipe['id']}/'>{recipe['name']}</a> - {recipe['minutes']} wuti</li>"
        for recipe in recipes
    )

    return page(name, f"<ul>{items}</ul>")

def search(request):
    q = request.GET.get("q", "")

    if not q:
        return page("dzebna", "chawere sadziebo sityva")

    recipes = [
        recipe for recipe in RECIPES
        if any(q in ingredient for ingredient in recipe["ingredients"])
    ]

    items = "",join(
        f"<li><a href='/recipes/{recipe['id']}/'>{recipe['name']}</a></li>"
        for recipe in recipes
    )

    return page("dzebnis shedegebi", f"<ul>{items}</ul>")
