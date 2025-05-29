from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

def home(request):
    return render(request, 'recipe/home.html')


def recipes(request):
    all_recipes = Recipe.objects.all()
    context = {"recipes": all_recipes}
    return render(request, 'recipe/recipes.html', context) 


def newrecipe(request):
    context = {}  # Always define context upfront

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
        


        return redirect('/newrecipe/')

    return render(request, 'recipe/newrecipe.html', context)
