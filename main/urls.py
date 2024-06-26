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
    path('tm/product/<pk>', views.product, name="product"),
    path('tm/contact/', views.contact, name="contact"),
    path('tm/contact/send_email/', views.send_email, name="send_email"),
    

    #russiann
    path('ru/', views.index_russian,name="index_russian"),
    path('ru/services/', views.services_russian, name="services_russian"),
    path('ru/services/<pk>', views.service_russian, name="service_russian"),
    path('ru/it_services/', views.it_services_russian, name="it_services_russian"),
    path('ru/it_services/<pk>', views.it_service_russian, name="it_service_russian"),
    path('ru/products/', views.products_russian, name="products_russian"),
    path('ru/product/<pk>', views.product_russian, name="product_russian"),
    path('ru/contact/', views.contact_russian, name="contact_russian"),
    path('ru/contact/send_email/', views.send_email_russian, name="send_email_russian"),

]
