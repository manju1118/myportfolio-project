from django.shortcuts import render

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
    return render(request, 'portfolio/contact.html')


#project view

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