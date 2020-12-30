from django.shortcuts import render
from .models import About, Choose, Chef


def about(request):
    about = About.objects.all()
    choose = Choose.objects.all()
    chefs = Chef.objects.all()

    context = {'about': about, 'choose': choose, 'chefs': chefs}

    return render(request, 'about/about.html', context)


