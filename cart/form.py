from django import forms
from django.shortcuts import get_object_or_404

from shop.models import Product


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 50)]
    quantity = forms.TypedChoiceField(
        label="Quantité",
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

# class CartAddProductForm(forms.Form):
#     def __init__(self, quantity, *args, **kwargs):
#         super(CartAddProductForm, self).__init__(*args, **kwargs)
#         # quantity = [(str(i)) for i in range(1, self.quantity + 1)]
#         self.fields['quantity'].choices = quantity
#
#     quantity = forms.ChoiceField(choices=(), required=True)
#     update = forms.BooleanField(required=False,
#                                 initial=False,
#                                 widget=forms.HiddenInput)