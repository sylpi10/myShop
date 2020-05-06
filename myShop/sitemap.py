from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from shop.models import Product


class FlatPageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return FlatPage.objects.all()


class ProdSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Product.objects.all()
