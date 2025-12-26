from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    email = forms.CharField(required=True)
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            return forms.ValidationError("Password did not match with confirm password")

    



class LoginForm(forms.Form):
    #widget is only used when django forms are rendered on frontend
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        if not username:
            username = email
        if not username and not email:
            return forms.ValidationError("A username or Email is required")
        return cleaned_data

    
