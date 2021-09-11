from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Suggestions 
from django import forms


class CreateUserForm(UserCreationForm):
    """
    This class is used to create the registration page.
    :param request: it's a form request from user.
    """
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']

class SuggestionForm(forms.Form):
    """
    :param request: it's a form request from user.
    """
    class Meta:
        model= Suggestions
        fields= ['first_name', 'last_name', 'email', 'message']