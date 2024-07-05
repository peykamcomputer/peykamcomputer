from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages

from .models import Aboutus, Stats, FAQ, HeroSection, Service, Category, Product, Slider, ITservice, FileUploadInstruction, CartItem, OrderProduct
# Create your views here.

###turkmen langugage
def index(request):
    page = "home"
    language = "turkmen"
    aboutus = Aboutus.objects.last()
    services = Service.objects.all()
    stats = Stats.objects.last()
    faqs = FAQ.objects.all()
    hero_section = HeroSection.objects.last()
    sliders = Slider.objects.all()
    current_url = request.get_full_path()
    
    context = {
        'page': page, 
        'language': language,
        'aboutus': aboutus, 
        'services': services,
        'stats': stats,
        'faqs': faqs,
        'hero_section': hero_section,
        'sliders': sliders,
        'current_url': current_url
    }
    context['title_name'] = "Peykam | Baş sahypa"
    return render(request, 'turkmen/index.html', context)

#services section
def services(request):
    page = "services"
    language = "turkmen"
    services = Service.objects.all()
    context = {
        'page': page,
        'language': language,
        'services': services,
    }
    context['title_name'] = "Peykam | Hyzmatlar"
    return render(request, 'turkmen/services.html', context)


def service(request, pk):
    page = "services"
    language = "turkmen"
    service = Service.objects.get(id=pk)
    services = Service.objects.all()
    context = {
        'page': page,
        'language': language,
        'service': service,
        'services': services
    }
    context['title_name'] = f"Peykam | Hyzmatlar | {service.title}"
    return render(request, 'turkmen/service-details.html', context)


#it services section
def it_service(request, pk):
    page = "it_services"
    language = "turkmen"
    it_service = ITservice.objects.get(id=pk)
    it_services = ITservice.objects.all()
    context = {
        'page': page,
        'language': language,
        'it_service': it_service,
        'it_services': it_services
    }
    context['title_name'] = f"Peykam | IT Hyzmatlar | {it_service.title}"
    return render(request, 'turkmen/it-service-details.html', context)

def it_services(request):
    page = "it_services"
    language = "turkmen"
    it_services = ITservice.objects.all()
    context = {
        'page': page,
        'language': language,
        'it_services': it_services
    }
    context['title_name'] = "Peykam | IT Hyzmatlar"
    return render(request, 'turkmen/it_services.html', context)


#products section
def products(request):
    page = "products"
    language = "turkmen"
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'page': page,
        'language': language,
        'categories': categories,
        'products': products
    }
    context['title_name'] = "Peykam | Harytlar"
    return render(request, 'turkmen/products.html', context)

def category_products(request, pk):
    page = "category products"
    language = "turkmen"
    product_category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    products = Product.objects.filter(category=product_category)
    context = {
        'page': page,
        'language': language,
        'categories': categories,
        'products': products,
        'product_category': product_category
    }
    context['title_name'] = "Peykam | Harytlar"
    return render(request, 'turkmen/products.html', context)

def product(request, pk):
    page = "products"
    language = "turkmen"
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    context = {
        'page': page,
        'language': language,
        'product': product,
        'products': products
    }
    context['title_name'] = f"Peykam | Harytlar | {product.name}"
    return render(request, 'turkmen/product-details.html', context)


def view_cart(request):
    page = "cart"
    language = "turkmen"
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'page': page,
        'language': language,
        'cart_items': cart_items, 
        'total_price': total_price
    }
    context['title_name'] = f"Peykam | Harytlar | Sebet"
    return render(request, 'turkmen/cart.html', context)
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('products')

def increase_quantity(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def decrease_quantity(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.quantity -= 1
    
    if cart_item.quantity == 0:
        cart_item.delete()
        return redirect('view_cart')
    
    cart_item.save()
    return redirect('view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def order_products(request):
    page = "cart"
    language = "turkmen"
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'page': page,
        'language': language,
        'cart_items': cart_items,
        'total_price': total_price
    }
    context['title_name'] = f"Peykam | Harytlar | Sargamak"
    return render(request, 'turkmen/order-page.html', context)

def send_order(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    ordered_products = ""
    for item in list(cart_items):
        ordered_products += (f"{item.product.name} - {item.quantity}x. ")

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')

        order_object = OrderProduct.objects.create(name=name, address=address, email=email, phone=phone_number, products=ordered_products, total_price=total_price)
        order_object.save()
        cart_items.delete()

        formdata = {'date': order_object.date_added.strftime("%d-%m-%Y %H:%M:%S"), 'name': name, 'phone_number': phone_number, 'address': address, 'email': email, 'ordered_products': ordered_products, 'total_price': total_price}
        message = '''
        Sargydyň senesi: \t{}\n
        Ady we familiýasy:\t{}\n
        Telefon belgisi:\t{}\n
        Öý salgysy:\t{}\n
        Email salgysy:\t{}\n
        Sargalan harytlar:\t{}\n
        Jemi baha:\t{}\n
        
        '''.format(formdata['date'], formdata['name'], formdata['phone_number'], formdata['address'], formdata['email'], formdata['ordered_products'], formdata['total_price'])
        subject = f"Peykam Web. Müşderi haryt sargydy №{order_object.uid}!"

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        try: 
            email.send()
            messages.success(request, f"Siziň sargydyňyz №{order_object.uid} belgi bilen üstünlikli kabul edildi. Biz siziň bilen gysga wagtda habarlaşarys.")
            return redirect("order_products")
        except:
            messages.error(request, "Ýalňyşlyk! Sargydyňyz käbir sebäplere kabul edilmedi.")
            return redirect("order_products")   


#contact section
def contact(request):
    page = "contact"
    language = "turkmen"
    context = {
        'page': page,
        'language': language,
    }
    context['title_name'] = "Peykam | Habarlaşmak üçin"
    return render(request, 'turkmen/contact.html', context)

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        problem = request.POST.get('problem')

        formdata = {'name': name, 'phone_number': phone_number, 'email': email, 'problem': problem}
        message = '''
        Ady we familiýasy:\t{}\n
        Telefon belgisi:\t{}\n
        Email salgysy:\t{}\n
        Meselesi:\t{}\n
        '''.format(formdata['name'], formdata['phone_number'], formdata['email'], formdata['problem'])
        subject = "Peykam Web. Müşderi haty!"

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        try: 
            email.send()
            messages.success(request, "Siziň e-mail hatyňyz üstünlikli ugradyldy. Biz siziň bilen gysga wagtda habarlaşarys.")
            return redirect("contact")
        except:
            messages.error(request, "Ýalňyşlyk! E-mail hatyňyz käbir sebäplere görä ugradylmady.")
            return redirect("contact")


#online translation section
def translation_page(request):
    page = "translation"
    language = "turkmen"
    upload_instructions = FileUploadInstruction.objects.all()
    context = {
        'page': page,
        'language': language,
        'upload_instructions': upload_instructions
    }
    context['title_name'] = "Peykam | Onlaýn terjime"
    return render(request, 'turkmen/translation-page.html', context)


def send_translation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        files = request.FILES.getlist('file')

        formdata = {'name': name, 'phone_number': phone_number, 'email': email, 'problem': problem}
        message = '''
        Ady we familiýasy:\t{}\n
        Telefon belgisi:\t{}\n
        Email salgysy:\t{}\n
        Meselesi:\t{}\n
        Müşderiniň resminamalarynyň faýllary:\n
        '''.format(formdata['name'], formdata['phone_number'], formdata['email'], formdata['problem'])
        subject = "Peykam Web. Onlaýn terjime sargytnama!"

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])

        try: 
            for file in files:
                file_name = file.name
                file_type = file.content_type
                file_content = file.read()
                email.attach(file_name, file_content, file_type)
            email.send()
            messages.success(request, "Siziň resminamalaryňyz üstünlikli ugradyldy. Biz siziň bilen gysga wagtda habarlaşarys.")
            return redirect("translation_page")
        except:
            messages.error(request, "Ýalňyşlyk! Resminamalaryňyz käbir sebäplere görä ugradylmady.")
            return redirect("translation_page")




###russian language
def index_russian(request):
    page = "home"
    language = "russian"
    aboutus = Aboutus.objects.last()
    services = Service.objects.all()
    stats = Stats.objects.last()
    faqs = FAQ.objects.all()
    hero_section = HeroSection.objects.last()
    sliders = Slider.objects.all()
    
    context = {
        'page': page, 
        'language': language,
        'aboutus': aboutus, 
        'services': services,
        'stats': stats,
        'faqs': faqs,
        'hero_section': hero_section,
        'sliders': sliders
    }
    context['title_name'] = "Peykam | Главная страница"
    return render(request, 'russian/index.html', context)



#services section
def services_russian(request):
    page = "services"
    language = "russian"
    services = Service.objects.all()
    context = {
        'page': page,
        'language': language,
        'services': services
    }
    context['title_name'] = "Peykam | Услуги"
    return render(request, 'russian/services.html', context)


def service_russian(request, pk):
    page = "services"
    language = "russian"
    service = Service.objects.get(id=pk)
    services = Service.objects.all()
    context = {
        'page': page,
        'language': language,
        'service': service,
        'services': services
    }
    context['title_name'] = f"Peykam | Услуги | {service.title_russian}"
    return render(request, 'russian/service-details.html', context)


#it services section
def it_service_russian(request, pk):
    page = "it_services"
    language = "russian"
    it_service = ITservice.objects.get(id=pk)
    it_services = ITservice.objects.all()
    context = {
        'page': page,
        'language': language,
        'it_service': it_service,
        'it_services': it_services
    }
    context['title_name'] = f"Peykam | IT Услуги | {it_service.title_russian}"
    return render(request, 'russian/it-service-details.html', context)

def it_services_russian(request):
    page = "it_services"
    language = "russian"
    it_services = ITservice.objects.all()
    context = {
        'page': page,
        'language': language,
        'it_services': it_services
    }
    context['title_name'] = "Peykam | IT Услуги"
    return render(request, 'russian/it_services.html', context)

#products section
def products_russian(request):
    page = "products"
    language = "russian"
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'page': page,
        'language': language,
        'categories': categories,
        'products': products
    }
    context['title_name'] = "Peykam | Товары"
    return render(request, 'russian/products.html', context)


def category_products_russian(request, pk):
    page = "category products"
    language = "russian"
    product_category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    products = Product.objects.filter(category=product_category)
    context = {
        'page': page,
        'language': language,
        'categories': categories,
        'products': products,
        'product_category': product_category
    }
    context['title_name'] = "Peykam | Товары"
    return render(request, 'russian/products.html', context)


def product_russian(request, pk):
    page = "products"
    language = "russian"
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    context = {
        'page': page,
        'language': language,
        'product': product,
        'products': products
    }
    context['title_name'] = f"Peykam | Товары | {product.name_russian}"
    return render(request, 'russian/product-details.html', context)

def view_cart_russian(request):
    page = "cart"
    language = "russian"
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'page': page,
        'language': language,
        'cart_items': cart_items, 
        'total_price': total_price
    }
    context['title_name'] = f"Peykam | Товары | Корзина"
    return render(request, 'russian/cart.html', context)
 
def add_to_cart_russian(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('products_russian')

def increase_quantity_russian(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart_russian')

def decrease_quantity_russian(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.quantity -= 1
    
    if cart_item.quantity == 0:
        cart_item.delete()
        return redirect('view_cart_russian')
    
    cart_item.save()
    return redirect('view_cart_russian')
 
def remove_from_cart_russian(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart_russian')


def order_products_russian(request):
    page = "cart"
    language = "russian"
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'page': page,
        'language': language,
        'cart_items': cart_items,
        'total_price': total_price
    }
    context['title_name'] = f"Peykam | Товары | Заказать"
    return render(request, 'russian/order-page.html', context)

def send_order_russian(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    ordered_products = ""
    for item in list(cart_items):
        ordered_products += (f"{item.product.name_russian} - {item.quantity}x. ")

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')

        order_object = OrderProduct.objects.create(name=name, address=address, email=email, phone=phone_number, products=ordered_products, total_price=total_price)
        order_object.save()
        cart_items.delete()

        formdata = {'date': order_object.date_added.strftime("%d-%m-%Y %H:%M:%S"), 'name': name, 'phone_number': phone_number, 'address': address, 'email': email, 'ordered_products': ordered_products, 'total_price': total_price}
        message = '''
        Дата заказа: \t{}\n
        Имя и фамилия:\t{}\n
        Номер телефона:\t{}\n
        Адрес:\t{}\n
        Email:\t{}\n
        Заказанные товары:\t{}\n
        Общая стоимость:\t{}\n
        
        '''.format(formdata['date'], formdata['name'], formdata['phone_number'], formdata['address'], formdata['email'], formdata['ordered_products'], formdata['total_price'])
        subject = f"Peykam Web. Заказ клиента №{order_object.uid}!"

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        try: 
            email.send()
            messages.success(request, f"Ваш заказ №{order_object.uid} успешно принят. Мы свяжемся с Вами в скором времени.")
            return redirect("order_products_russian")
        except:
            messages.error(request, "Ошибка! Ваш заказ по какой-то причине не был принят.")
            return redirect("order_products_russian")   

#contact section
def contact_russian(request):
    page = "contact"
    language = "russian"
    context = {
        'page': page,
        'language': language,
    }
    context['title_name'] = "Peykam | Обратная связь"
    return render(request, 'russian/contact.html', context)

def send_email_russian(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        problem = request.POST.get('problem')

        formdata = {'name': name, 'phone_number': phone_number, 'email': email, 'problem': problem}
        message = '''
        Имя и фамилия:\t{}\n
        Номер телефона:\t{}\n
        Email:\t{}\n
        Проблема:\t{}\n
        '''.format(formdata['name'], formdata['phone_number'], formdata['email'], formdata['problem'])
        subject = 'Peykam Web. Письмо Клиента!'

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        try: 
            email.send()
            messages.success(request, "Ваше письмо было успешно отправлено. Мы свяжемся с вами в скором времени.")
            return redirect("contact_russian")
        except:
            messages.error(request, "Ошибка! Ваше письмо не было отправлено по какой-то причине.")
            return redirect("contact_russian")


#online translation section
def translation_page_russian(request):
    page = "translation"
    language = "russian"
    upload_instructions = FileUploadInstruction.objects.all()
    context = {
        'page': page,
        'language': language,
        'upload_instructions': upload_instructions
    }
    context['title_name'] = "Peykam | Онлайн перевод"
    return render(request, 'russian/translation-page.html', context)



def send_translation_russian(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        files = request.FILES.getlist('file')

        formdata = {'name': name, 'phone_number': phone_number, 'email': email, 'problem': problem}
        message = '''
        Имя и фамилия:\t{}\n
        Номер телефона:\t{}\n
        Email:\t{}\n
        Проблема:\t{}\n
        Файлы документа клиента:\n
        '''.format(formdata['name'], formdata['phone_number'], formdata['email'], formdata['problem'])
        subject = "Peykam Web. Заявка на онлайн перевод!"

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        
        try: 
            for file in files:
                file_name = file.name
                file_type = file.content_type
                file_content = file.read()
                email.attach(file_name, file_content, file_type)
            email.send()
            messages.success(request, "Ваше данные были успешно отправлены. Мы свяжемся с вами в скором времени.")
            return redirect("translation_page_russian")
        except:
            messages.error(request, "Ошибка! Ваши документы по каким-то причинам не были отправлены.")
            return redirect("translation_page_russian")

