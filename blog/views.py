from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  )

# .models import Post
# .(current directory) -> models -> Post
from blog.models import Post

# Create your views here.
# view = page
# A view always return an HTTP Response or an Exception.

# Class based views, kinds of class based views ->
# https://youtu.be/-s7e_Fy6NRU?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=66


def home(request):
    # function based view - not in use , PostListView is in use.
    context = {
        'posts': Post.objects.all(),
    }
    # django needs the path from the templates folder in current app to the specific template
    return render(request, 'blog/home.html', context)


def about(request):
    # function based view
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListView(ListView):
    # class based view - list view - to list all posts
    # model tells our ListView what model to query in order to create the list,
    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model
    model = Post

    # replacing default template naming convention -> <app>/<model>_<viewtype>.html
    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name
    template_name = 'blog/home.html'

    # by default ListView class will do object_list = Post.objects.all()
    # instead of posts = Post.objects.all()
    # let the class know we want to call it 'posts' instead of 'object_list'
    # override attribute 'context_object_name'
    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name
    context_object_name = 'posts'  # same as our function view, line 19

    # Change order from newest post to oldest post , change query
    # ordering attribute = field we want to order on
    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    # detail view to get a specific post
    # this class based view will follow the naming conventions to see how less code we write, compare to PostListView where we broke the conventions
    model = Post
    # template naming convention = <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    # LoginRequiredMixin -> user should be logged in to access this page

    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#createview
    # That will be a view with a form where we create a new post
    # so the other thing we need to provide is the
    model = Post
    fields = ['title', 'content']

    #  override the form valid method, so that we add author before a form is submitted
    def form_valid(self, form):
        # take the form instance before submitting and set the author to the current logged in user
        form.instance.author = self.request.user
        # now validate the form
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # almost same as PostCreateView
    # LoginRequiredMixin -> user should be logged in to access this page

    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#createview
    # That will be a view with a form where we create a new post
    # so the other thing we need to provide is the
    model = Post
    fields = ['title', 'content']

    #  override the form valid method, so that we add author before a form is submitted
    def form_valid(self, form):
        # take the form instance before submitting and set the author to the current logged in user
        form.instance.author = self.request.user
        # now validate the form
        return super().form_valid(form)
