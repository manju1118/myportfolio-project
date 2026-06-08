from django.contrib import messages

from django.shortcuts import redirect, render
from .models import Category, Post


#home page view
def blog_homepage(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }   
    return render(request, 'blog/blog_homepage.html', context)


#post create view

def blog_create(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category = Category.objects.get(id=category_id)
        Post.objects.create(
            category=category,
            title=title,
            content=content,
            image=image,
            author=request.user
        )
        messages.success(request, 'Post created successfully!')
        return redirect('blog_homepage')
    categories = Category.objects.all()
    context = {
        'categories': categories
    }   
    return render(request, 'blog/blog_create.html', context)

#category page view

def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = category.posts.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'category': category,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'blog/category_posts.html', context)



#post detail view


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    context = {
        'post': post,
        
    }
    return render(request, 'blog/post_detail.html', context)