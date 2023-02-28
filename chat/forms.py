from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise ValidationError('Username cannot be empty.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if not password1:
            raise ValidationError('Password cannot be empty.')
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if not password2:
            raise ValidationError('Password confirmation cannot be empty.')
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.')
        return cleaned_data
