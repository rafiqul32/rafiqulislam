from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Flat, Rent


class FlatModelForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = [
            'flat_code',
            'resident_name',
            'monthly_rent'
        ]


class RentModelForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = [
            'id',
            'flat',
            'month',
            'rent',
            'rent_paid',
            'elec_bill',
            'elec_bill_paid'
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
