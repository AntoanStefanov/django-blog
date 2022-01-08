from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    # views.home handles this route ''
    # replacing views.home with PostListView
    # convert the class into an actual view with .as_view() method, execute it
    path('', PostListView.as_view(), name='blog_home'),
    # views.about handles this route 'about/'
    path('about/', views.about, name='blog_about'), 
]


# django checks template in this pattern <app>/<model>_<viewtype>.html -> blog/post_list.html
# we could create a template with this naming convention and it would see that temolate
# But we could change wihch template this view to use, let's do it with the template we have for our home view.