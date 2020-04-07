from django import forms
from shop.models import Product


class CartAddProductForm(forms.Form):

    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 12)]

    quantity = forms.TypedChoiceField(
        label="Quantité",
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    # print(quantity.choices)
    # print(quant_max)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

# for p in Product.objects.all():
#     quant_max = p.quantity + 1
#     print(p.name)
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, quant_max)]
