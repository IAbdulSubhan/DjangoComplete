from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import *

def home(request):
    return render(request, 'recipe/home.html')


def recipes(request):
    all_recipes = Recipe.objects.all()

    #search functionality
    query = request.GET.get('search')
    if query:
        all_recipes = Recipe.objects.filter(title__icontains=query)
    else:
        all_recipes = Recipe.objects.all()

    context = {"recipes": all_recipes}
    return render(request, 'recipe/recipes.html', context) 

def delrecipe(reqest, id):
    recipe = get_object_or_404(Recipe, id = id)
    recipe.delete()
    return redirect("recipes")

def newrecipe(request):
    context = { }
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        #print(context)  # Optional: for debugging
        #save the data object
        Recipe.objects.create(
            title= title,
            description= description,
            image= image,
        )
        


        return redirect('recipes')

    return render(request, 'recipe/newrecipe.html', context)

def show(request, id):
    recipe_det = get_object_or_404(Recipe, id=id)
    context = {"recipe": recipe_det}
    return render(request, 'recipe/show.html', context)

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")


        recipe.title = title
        recipe.description = description

        if image:
            recipe.image = image


        recipe.save()

        return redirect('recipes')

    context = {"recipe": recipe}
    return render(request, 'recipe/update_recipe.html', context)