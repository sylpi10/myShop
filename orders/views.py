from django.shortcuts import render, redirect
from django.urls import reverse

from cart.cart import Cart
from orders.form import OrderCreateForm
from orders.models import OrderItem
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount='{:.0f}'.format(cart.get_total_price() * 100),
            currency='EUR',
            description="Paiement par CB",
            source=request.POST['stripeToken']
        )
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # clear the cart
            cart.clear()

            # redirect
            request.session.modified = True

            order.paid = True

            # TODO : change model product quantity ??

            order.save()

            return redirect('payment:done')
        else:
            return redirect('payment:canceled')

            # return render(request,
            #               'orders/order/created.html',
            #               {'order': order})
    else:
        form = OrderCreateForm()
        key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'key': key, 'form': form})
