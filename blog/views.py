from django.shortcuts import render

# Create your views here.
# view = page
# A view always return an HTTP Response or an Exception.

# dummy data
posts = [
    {
        'author': 'John',
        'title': 'Blog Post 1',
        'content': 'This is a blog post 1',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Mary',
        'title': 'Blog Post 2',
        'content': 'This is a blog post 2',
        'date_posted': 'August 11, 2018'
    },
    {
        'author': 'Tony',
        'title': 'Blog Post 3',
        'content': 'This is a blog post 3',
        'date_posted': 'August 16, 2018'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    # django needs the path from the templates folder in current app to the specific template
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
