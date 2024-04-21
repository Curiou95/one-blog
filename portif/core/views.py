from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')
def blog(request):
    return render(request, 'core/blog.html')
def projects(request):
    return render(request, 'core/projects.html')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')