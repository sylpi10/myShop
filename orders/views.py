from django.core import mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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

            subject = 'Nouvelle commande'
            html_message = render_to_string('orders/order/send_mail.html', {'cart': cart, 'item': item})
            plain_message = strip_tags(html_message)
            from_email = 'syl.pillet@hotmail.fr'
            to = 'syl.pillet@hotmail.fr'

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

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
