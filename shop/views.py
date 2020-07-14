from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Product, ProductImage
from cart.form import CartAddProductForm
from django.core.paginator import Paginator
from shop.forms import TestForm
from django.urls import reverse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    productspag = Product.objects.filter(available=True).order_by('-updated')
    # request.session.set_expiry(20)
#     if request.session.is_empty():
#         messages.success(request, 'La session a expiré')

    # pagination
    paginator = Paginator(productspag, 8)
    page = request.GET.get('page')
    productspag = paginator.get_page(page)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        productspag = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'productspag': productspag,
                   'products': products,
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    quantity = [(str(i)) for i in range(1, product.quantity+1)]
    photos = ProductImage.objects.filter(product=product)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'quantity': quantity,
                   'photos': photos
                   })



# routing
def about(request):
    return render(request,
                  'shop/about.html')


def contact(request):
     if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():

            subject = 'Nouveau Mail de {}  depuis l\'Atelier Chenoa, Objet : {} '.format(form.cleaned_data['name'].capitalize(), form.cleaned_data['subject'], )
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            print('email', form.cleaned_data['email'])
            send_mail(subject, message, from_email, ['syl.pillet@hotmail.fr'])
#             return HttpResponseRedirect(reverse('thanks'))
            messages.success(request, 'Votre message a bien été envoyé')
            return HttpResponseRedirect('contact')

     else:
        form = TestForm()
     return render(request, 'shop/contact.html', {'form': form})


def legals(request):
    return render(request,
                  'shop/legals.html')


def cgv(request):
    return render(request,
                  'shop/cgv.html')

