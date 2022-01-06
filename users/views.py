from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views/pages here. Business logic is here also.


def register(request):
    # https://docs.djangoproject.com/en/4.0/topics/forms/#the-view
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # to save/create a new user in DB -> form.save()
            # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#the-save-method
            form.save()
            data = form.cleaned_data
            messages.success(request, f'Your account has been created! Your are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# require a user to be logged in before seeing this profile view
# decorator -> adds functionality to an existing function
# in this case, adds functionality to our profile view
# where the user must be logged in to view this page
@login_required
def profile(request):
    return render(request, 'users/profile.html')