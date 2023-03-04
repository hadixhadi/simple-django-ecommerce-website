from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class registerForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']

    #email validation
    def clean_email(self):
        email=self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email is already exist')
        return email