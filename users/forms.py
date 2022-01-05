from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label=("Email"))

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
