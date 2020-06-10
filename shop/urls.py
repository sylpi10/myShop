from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('about', views.about, name='about'),
    path('legals', views.legals, name='legals'),
    path('contact', views.contact, name='contact'),
    path('cgv', views.cgv, name='cgv'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]

