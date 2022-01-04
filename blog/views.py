from django.shortcuts import render

# .models import Post
# .(current directory) -> models -> Post
from blog.models import Post

# Create your views here.
# view = page
# A view always return an HTTP Response or an Exception.

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    # django needs the path from the templates folder in current app to the specific template
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
