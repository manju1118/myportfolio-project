from django.shortcuts import render, redirect
from blogproject.models import Post
from portfolio_app.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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


@login_required
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
    return render(request,'accounts/user_dashboard.html')
@login_required
def user_settings_page(request):
    return render(request,'accounts/user_settings.html')

