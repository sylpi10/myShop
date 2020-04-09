from django import forms
from django.shortcuts import get_object_or_404

from shop.models import Product


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 12)]
    quantity = forms.TypedChoiceField(
        label="Quantité",
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

