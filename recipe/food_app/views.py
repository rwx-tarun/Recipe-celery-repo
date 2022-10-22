import re
from django.shortcuts import render
from food_app.models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from recipe.settings import CACHE_TTL

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


def get_recipe(filter_recipe = None):
    recipe = Recipe.objects.all()
    if filter_recipe:
        print("************* DATA FROM DB **************")
        recipe = recipe.filter(name__icontains = filter_recipe)
    else:
        recipe = Recipe.objects.all()
    return recipe


def show_food_list(request):
    filter_recipe = request.GET.get('recipe')
    if cache.get(filter_recipe):
        recipe = cache.get(filter_recipe)
        print("************* DATA FROM CACHE **************")
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe , recipe)
        else:
            recipe = get_recipe()

    context = {
        'recipe':recipe
    }
    return render(request,  'home.html' , context)

def show_detail(request,id):
    recipe = Recipe.objects.get(id=id)
    context = {
        "recipe":recipe
    }
    return render(request , "detail.html" , context)