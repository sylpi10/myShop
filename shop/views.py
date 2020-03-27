from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.form import CartAddProductForm
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    productspag = Product.objects.filter(available=True)

    # pagination
    paginator = Paginator(productspag, 4)
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
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})

