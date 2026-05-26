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