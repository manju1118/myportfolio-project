from django.contrib import messages

from django.shortcuts import redirect, render
from .models import Category, Post, Like, Comment
from django.contrib.auth.decorators import login_required


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
    comments = post.comments.all().order_by('-created_at')
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(post=post, author=request.user).exists()
    context = {
        'post': post,
        'comments': comments,
        'liked': liked
        
    }
    return render(request, 'blog/post_detail.html', context)


def post_update(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category = Category.objects.get(id=category_id)
        post.category = category
        post.title = title
        post.content = content
        if image:
            post.image = image
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post_detail', slug=post.slug)
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'blog/post_update.html', context)


def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('blog_homepage')

#like post view

@login_required
def like_post(request, slug):
    post = Post.objects.get(slug=slug)
    like, created = Like.objects.get_or_create(post=post, author=request.user)
    if not created:
        like.delete()
        messages.info(request, 'You unliked the post.')
    else:
        messages.success(request, 'You liked the post.')

    return redirect('blog_homepage')

#add comment view

@login_required
def add_comment(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
        messages.success(request, 'Comment added successfully!')
    return redirect('post_detail', slug=slug)