from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views/pages here. Business logic is here also.


def register(request):
    # https://docs.djangoproject.com/en/4.0/topics/forms/#the-view
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            messages.success(request, f'Account created for {data["username"]}!')
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
