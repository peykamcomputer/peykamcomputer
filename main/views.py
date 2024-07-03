from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Aboutus, Stats, FAQ, HeroSection, Service, Category, Product, Slider, ITservice, FileUploadInstruction
# Create your views here.

#turkmen
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
        email.send()
        
        messages.success(request, "Siziň e-mail hatyňyz üstünlikli ugradyldy. Biz siziň bilen gysga wagtda habarlaşarys")
        return redirect("contact")

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
        for file in files:
            file_name = file.name
            file_type = file.content_type
            file_content = file.read()
            email.attach(file_name, file_content, file_type)
        email.send()

        messages.success(request, "Siziň resminamalaryňyz üstünlikli ugradyldy. Biz siziň bilen gysga wagtda habarlaşarys")
        return redirect("translation_page")




#russian
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
        send_mail('Peykam Web. Письмо Клиента!', message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
        
        messages.success(request, "Ваше письмо было успешно отправлено. Мы свяжемся с вами в скором времени")
        return redirect("contact_russian")



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
        for file in files:
            file_name = file.name
            file_type = file.content_type
            file_content = file.read()
            email.attach(file_name, file_content, file_type)
        email.send()

        messages.success(request, "Ваше данные были успешно отправлены. Мы свяжемся с вами в скором времени")
        return redirect("translation_page_russian")
