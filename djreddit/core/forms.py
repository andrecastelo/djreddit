from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=64)
    password = forms.CharField(label='Password', required=True)
