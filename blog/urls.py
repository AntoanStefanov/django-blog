from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    )
from . import views

urlpatterns = [
    # views.home handles this route ''
    # replacing views.home with PostListView
    # convert the class into an actual view with .as_view() method, execute it
    path('', PostListView.as_view(), name='blog_home'),

    # route with a variable -> post pk which is the id
    # we can grab the value from the url and use it in the view class
    # variable = pk becuase that is what the DetailView expects to be in order to grab the specific object
    # we can change it but we have to add attribute in our class
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # views.about handles this route 'about/'
    path('about/', views.about, name='blog_about'),

]


# django checks template in this pattern <app>/<model>_<viewtype>.html -> blog/post_list.html
# we could create a template with this naming convention and it would see that temolate
# But we could change wihch template this view to use, let's do it with the template we have for our home view.
