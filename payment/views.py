from django.shortcuts import render

from cart.cart import Cart
from orders.form import OrderCreateForm
from orders.models import OrderItem, Order


def payment_done(request):
    return render(request, 'order/created.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


