from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)

        """
        def save(self):
            data = self.cleaned_data
            user = User(username = data['username'], password = data['password'],
                    first_name = data['first_name'], email = data['email'])
            user.save()
            userProfile = Profile(user = user, location = data['location'])
            userProfile.save()
        """
