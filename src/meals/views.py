from django.shortcuts import render
from .models import Meal, Category


def meal_list(request):
    meals = Meal.objects.all()
    categories = Category.objects.all()
    context = {'meals': meals, 'categories': categories}
    return render(request, 'meals/list.html', context)

def meal_detail(request, slug):
    meal = Meal.objects.get(slug=slug)
    context = {'meal': meal}
    return render(request, 'meals/detail.html', context)
