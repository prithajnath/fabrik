from django import forms

class RegisterForm(forms.Form):

    first_name = forms.CharField(
        required=True,
        label='firstname',
        max_length=32
        )

    username = forms.CharField(
        required=True,
        label='username',
        max_length=32
        )

    email = forms.EmailField(
        required=True,
        label='email',
        max_length=50
        )

    password = forms.CharField(
        required=True,
        label='password',
        max_length=32,
        widget=forms.PasswordInput()
        )

    location = forms.CharField(
        required=True,
        label='location',
        max_length=32
        )
