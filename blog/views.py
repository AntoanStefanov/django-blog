from django.shortcuts import render

# Create your views here.
# view = page
# A view always return an HTTP Response or an Exception.


def home(request):
    # django needs the path from the templates folder in current app to the specific template
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
