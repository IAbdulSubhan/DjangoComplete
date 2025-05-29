from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import *

def home(request):
    return render(request, 'recipe/home.html')


def recipes(request):
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

        # Save uploaded image
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        #print(context)  # Optional: for debugging
        #save the data object
        Recipe.objects.create(
            title= title,
            description= description,
            image= image_url,
        )
        


        return redirect('recipes')

    return render(request, 'recipe/newrecipe.html', context)

def show(request, id):
    recipe_det = get_object_or_404(Recipe, id=id)
    context = {"recipe": recipe_det}
    return render(request, 'recipe/show.html', context)
