from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category


# Create your views here.





def blog_homepage(request):
    posts = Post.objects.all().order_by('-created_at')

    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog_homepage.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-created_at')

    categories = Category.objects.all()
    

    context = {
        'posts': posts,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'blog/category_posts.html', context)

def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_detail.html', context)


