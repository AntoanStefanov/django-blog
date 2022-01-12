"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # chops of blog/ passes the rest to the given urls module
    # 'blog/' is a route

    # coding path like that, Blog app now is being the homepage of the entire website.
    # this will return the blog home page (making website home page same as home page of the blog app)
    # /about will hit this empty string and go to the about page of the blog, crazy stuff
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # DOCS LoginView ->
    # https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.views.LoginView.get_default_redirect_url
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

# https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
