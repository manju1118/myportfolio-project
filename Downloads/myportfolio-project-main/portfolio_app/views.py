from django.shortcuts import render, redirect
from blogproject.models import Category, Post, Like,Comment
from portfolio_app.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.


def homepage(request):
    return render(request, 'portfolio/homepage.html')

def about_page(request):
    return render(
        request, 'portfolio/about.html'
    )
def services(request):
    return render(request, 'portfolio/services.html')

def projects(request):
    return render(request, 'portfolio/projects.html')



def contact(request):
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('content')
        new_contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,

        )
        messages.success(request,'You have sent sucessfully!')
        new_contact.save()
        return redirect('contact')
    return render(request, 'portfolio/contact.html')


#projects view

def blog_project(request):
    return render(request, 'portfolio/blog_detail.html')

def ecommerce_project(request):
    return render(request,'portfolio/ecommerce_detail.html')

def todo_management(request):
    return render(request, 'portfolio/todo_management.html')

def personal_system(request):
    return render(request,'portfolio/personal_system.html')

def creative_portfolio(request):
    return render(request,'portfolio/creative_portfolio.html')

def corporate_business(request):
    return render(request,'portfolio/corporate_business.html')


#login and singup view

def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            messages.success(
                request, 'You Have Successfully LoggedIn!'
            )
            return redirect('homepage')
        else:
            messages.error(
                request, 'Invalid Username or Password!'
            )
    return render(request,'accounts/login.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect("register")

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(
            request,
            "Account created successfully"
        )

        return redirect("login")
    return render(request,'accounts/register.html')

def user_logout_page(request):
    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect('login')

@login_required
def user_profile_page(request):
    user_posts = Post.objects.filter(
        author=request.user
    ).order_by('-created_at')
    return render(request,'accounts/user_profile.html', {'user_posts': user_posts})



@login_required
def user_dashboard_page(request):

    user_posts = Post.objects.filter(
        author=request.user
    )

    total_posts = user_posts.count()

    total_categories = Category.objects.filter(
        posts__author=request.user
    ).distinct().count()

    total_comments = Comment.objects.filter(
        author=request.user
    ).count()

    total_likes = Like.objects.filter(
        post__author=request.user
    ).count()

    most_liked_post = user_posts.annotate(
        like_count=Count('likes')
    ).order_by('-like_count').first()

    latest_comments = Comment.objects.filter(
        post__author=request.user
    ).order_by('-created_at')[:5]

    recent_posts = user_posts.order_by(
        '-created_at'
    )[:5]

    context = {

        'total_posts': total_posts,
        'total_categories': total_categories,
        'total_comments': total_comments,
        'total_likes': total_likes,

        'most_liked_post': most_liked_post,

        'latest_comments': latest_comments,

        'recent_posts': recent_posts,

    }

    return render(
        request,
        'accounts/user_dashboard.html',
        context
    )
    
@login_required
def user_settings_page(request):
    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        user = request.user

        user.username = username
        user.email = email

        user.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect(
            "settings"
        )
    return render(request,'accounts/user_settings.html')

@login_required
def user_password_change_page(request):
    if request.method == "POST":

        current_password = request.POST.get(
            "old_password"
        )

        new_password1 = request.POST.get(
            "new_password1"
        )

        new_password2 = request.POST.get(
            "new_password2"
        )

        if not request.user.check_password(current_password):

            messages.error(
                request,
                "Current password is incorrect."
            )

            return redirect("password_change")

        if new_password1 != new_password2:

            messages.error(
                request,
                "New passwords do not match."
            )

            return redirect("password_change")

        request.user.set_password(new_password1)
        request.user.save()

        messages.success(
            request,
            "Password changed successfully."
        )

        return redirect("settings")
    return render(request,'accounts/user_password_change.html')

