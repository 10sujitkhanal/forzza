from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat your password'})
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "gender",
                  "is_superuser",
                  "is_staff",
                  "password1",
                  "password2")

        # widgets = {
        #     'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.TextInput(attrs={'placeholder': 'Repeat your password'}),
        # }

    def clean_username(self):
        username = self.cleaned_data['username']
        print(username)
        if ' ' in username:
            raise forms.ValidationError("Username can't contain spaces.")
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
