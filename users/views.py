from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views/pages here. Business logic is here also.


def register(request):
    # https://docs.djangoproject.com/en/4.0/topics/forms/#the-view
    if request.method == 'POST':
        # create instance and populate it with data from the request
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # to save/create a new user in DB -> form.save()
            # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#the-save-method
            form.save()
            messages.success(
                request, f'Your account has been created! Your are now able to log in')
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
    if request.method == 'POST':
        # leaving instances so Django would know which user and profile to update
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        # request.FILES
        #  -> additional data,
        #  -> file data coming in with the request,
        #  -> uploaded image from user.
        profile_update_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        # now we have both form populated with the data form the user,
        # check if the data is valid for both forms.
        #  if both are not valid , we dont send data
        #  just like in user registration form,
        #  but now we just have 2 form,
        #  but the process is almost identical
        # both must be valid
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(
                request, f'Your account has been updated!')
            # https://youtu.be/CQ90L5jfldw?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=843 redirect 
            return redirect('profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }

    return render(request, 'users/profile.html', context)
