from django import forms
from .models import Deposit


class DepositForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Deposit
        fields = ('deposit_amount', 'frozza_username', 'review', 'photo')
