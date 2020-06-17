from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category
from taggit.models import Tag
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.all()

    search = request.GET.get('search')
    if search:
        posts = posts.filter(
            Q(title__contains=search) | 
            Q(content__contains=search) | 
            Q(tags__name__contains=search)
        ).distinct()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts': posts}

    return render(request, 'blog/list.html', context)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    context = {'post': post, 'categories': categories, 'tags': tags, 'form': form}
    return render(request, 'blog/detail.html', context)

def post_by_tag(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    context = {'posts': posts}

    return render(request, 'blog/list.html', context)

def post_by_category(request, category):
    posts = Post.objects.filter(category__name=category)
    context = {'posts': posts}

    return render(request, 'blog/list.html', context)