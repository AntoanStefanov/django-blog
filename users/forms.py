from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # This class gives us a nested namespace for configurations
    # Keeps the configurations in one place
    # In within the configurations we say the model that will be affected
    # Example: when we do a form.save() it's going to save it to that given model
    # And the field we have in the list, are the fields that we want in the form and in what order

    class Meta:
        # specify the model that we want this form to interact with
        model = User
        # these are the fields that are going to be shown on the form (in what order also)
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # WHY WE NEED THIS ? WHEN A USER IS REGISTERED WE HAVE THAT FIELD FFS

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image'] # Corey writes down this as field = ['image']