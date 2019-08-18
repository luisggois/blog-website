from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

'''
In order to add a new field (email), we need to add that to the form itself,
for that we need to create a new form that inherits from our user form.
'''


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()  # By default it says that the email is mandatory

    class Meta:
        '''
        Gives nested name for configurations and keeps the configurations in one place
        And I'm saying that the model that is going to be affected is the User model,
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    ''' Create model form allowing to create a form that will work a specific database model '''

    email = forms.EmailField()  # By default it says that the email is mandatory

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
