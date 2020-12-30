from django.shortcuts import render
from meals.models import Meal, Category
from blog.models import Post
from about.models import Choose

def home(request):
    meals = Meal.objects.all()[:6]
    categories = Category.objects.all()
    posts = Post.objects.all()[:3]
    latest_post = Post.objects.last()
    choose = Choose.objects.all()

    context = {'meals': meals, 'categories': categories, 'posts': posts, 'latest_post': latest_post, 'choose': choose}

    return render(request, 'home/home.html', context)
