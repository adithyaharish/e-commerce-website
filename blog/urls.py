from django.urls import path
from .views import (ItemDetailView,HomeView,add_to_cart,remove_from_cart,
                    OrderSummaryView,remove_single_item_from_cart,CheckoutView,MyOrders)
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('my-orders/', MyOrders.as_view(), name='my_orders'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart')
]