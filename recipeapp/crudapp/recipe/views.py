from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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

@login_required(login_url = "login_page")
def delrecipe(reqest, id):
    recipe = get_object_or_404(Recipe, id = id)
    recipe.delete()
    return redirect("recipes")

@login_required(login_url = "login_page")
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

@login_required(login_url = "login_page")
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

def login_page(request):
    if request.method== "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username= username)
        if not user.exists():
            messages.info(request, "Invalid Username.")
            return redirect('login_page')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "Wrong username or Password.")
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('recipes')
        
    return render(request, 'recipe/login_page.html') 

def register(request):

    if request.method== "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username= username)
        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('register')

        
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "User registered Sucessfully.")
        return redirect('register')

    return render(request, 'recipe/register.html') 


def logout_page(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login_page')