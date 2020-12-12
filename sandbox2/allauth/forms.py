from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from .models import Order
from django.forms import TextInput

#import account.forms

"""class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]"""

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


