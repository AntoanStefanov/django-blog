from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views/pages here. Business logic is here also.


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
