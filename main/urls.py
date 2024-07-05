from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    #turkmen
    path('', views.index,name="index"),
    path('tm/', views.index,name="index"),
    path('tm/services/', views.services, name="services"),
    path('tm/services/<pk>', views.service, name="service"),
    path('tm/it_services/', views.it_services, name="it_services"),
    path('tm/it_services/<pk>', views.it_service, name="it_service"),
    path('tm/products/', views.products, name="products"),
    path('tm/products/<pk>', views.category_products, name="category_products"),
    path('tm/product/<pk>', views.product, name="product"),

    path('tm/cart/', views.view_cart, name='view_cart'),
    path('tm/cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('tm/cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('tm/cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('tm/cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('tm/cart/order', views.order_products, name='order_products'),
    path('tm/cart/order/send', views.send_order, name='send_order'),

    path('tm/contact/', views.contact, name="contact"),
    path('tm/contact/send_email/', views.send_email, name="send_email"),
    path('tm/translation_page/', views.translation_page, name="translation_page"),
    path('tm/translation_page/send_translation', views.send_translation, name="send_translation"),
    

    #russiann
    path('ru/', views.index_russian,name="index_russian"),
    path('ru/services/', views.services_russian, name="services_russian"),
    path('ru/services/<pk>', views.service_russian, name="service_russian"),
    path('ru/it_services/', views.it_services_russian, name="it_services_russian"),
    path('ru/it_services/<pk>', views.it_service_russian, name="it_service_russian"),
    path('ru/products/', views.products_russian, name="products_russian"),
    path('ru/products/<pk>', views.category_products_russian, name="category_products_russian"),
    path('ru/product/<pk>', views.product_russian, name="product_russian"),

    path('ru/cart/', views.view_cart_russian, name='view_cart_russian'),
    path('ru/cart/add/<int:product_id>/', views.add_to_cart_russian, name='add_to_cart_russian'),
    path('ru/cart/increase/<int:product_id>/', views.increase_quantity_russian, name='increase_quantity_russian'),
    path('ru/cart/decrease/<int:product_id>/', views.decrease_quantity_russian, name='decrease_quantity_russian'),
    path('ru/cart/remove/<int:item_id>/', views.remove_from_cart_russian, name='remove_from_cart_russian'),
    path('ru/cart/order', views.order_products_russian, name='order_products_russian'),
    path('ru/cart/order/send', views.send_order_russian, name='send_order_russian'),

    path('ru/contact/', views.contact_russian, name="contact_russian"),
    path('ru/contact/send_email/', views.send_email_russian, name="send_email_russian"),
    path('ru/translation_page/', views.translation_page_russian, name="translation_page_russian"),
    path('ru/translation_page/send_translation', views.send_translation_russian, name="send_translation_russian"),

]
