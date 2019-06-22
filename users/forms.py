from django import forms
from users.models import User
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=50,
                                required=True, label="Full Name", validators=[MinLengthValidator(3)])
    phoneNumber = forms.CharField(max_length=10, label="Phone Number", required=True,
                                  validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])

    class Meta:
        model = User
        fields = ['full_name', 'phoneNumber']
