from django.shortcuts import render
from django.views.generic import ListView

# .models import Post
# .(current directory) -> models -> Post
from blog.models import Post

# Create your views here.
# view = page
# A view always return an HTTP Response or an Exception.

# Class based views, kinds of class based views ->
# https://youtu.be/-s7e_Fy6NRU?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=66


def home(request):
    # function based view
    context = {
        'posts': Post.objects.all(),
    }
    # django needs the path from the templates folder in current app to the specific template
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # class based view
    # model tells our ListView what model to query in order to create the list,
    model = Post

    # replacing default template naming convention -> <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'

    # by default ListView class will do object_list = Post.objects.all()
    # instead of posts = Post.objects.all()
    # let the class know we want to call it 'posts' instead of 'object_list'
    # override attribute 'context_object_name'
    context_object_name = 'posts' # same as our function view, line 19 
    
    # Change order from newest post to oldest post , change query
    # ordering attribute = field we want to order on
    ordering = ['-date_posted']

def about(request):
    # function based view
    return render(request, 'blog/about.html', {'title': 'About'})
