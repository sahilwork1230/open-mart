from django import forms
from django.contrib.auth.models import User
from .models import Address
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class SignupForm(forms.ModelForm):
    # email = forms.CharField(required=True)
    # username = forms.CharField(required=True)
    # first_name = forms.CharField(required=True)
    password = forms.CharField(widget= forms.PasswordInput, required=True)
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","username", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        existing_email = User.objects.filter(email = email).exists()
        if existing_email:
            raise ValidationError("A user with this email already exists !")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match !")
        return cleaned_data

    



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
            raise forms.ValidationError("A username or Email is required")
        return cleaned_data



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ("user",)
    
