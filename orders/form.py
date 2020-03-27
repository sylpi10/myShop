from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["first_name", 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name': 'Votre Prénom',
            'last_name': 'Votre Nom',
            'email': 'Votre mail',
            'address': 'Votre Adresse',
            'postal_code': 'Code Postal',
            'city': 'Ville',
        }

