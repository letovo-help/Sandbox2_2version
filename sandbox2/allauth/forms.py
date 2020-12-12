from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from .models import Order
from django.forms import TextInput

import account.forms

"""class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]"""

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email = email).count()
        if user_count > 0:
            raise forms.ValidationError("Эта почта уже зарегистрирована")
        return email
