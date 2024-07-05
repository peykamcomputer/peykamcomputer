def context_data(request):
    from .models import Info, CartItem

    logo_name = Info.objects.last().logo_name
    title_name = Info.objects.last().title_name
    title_name_russian = Info.objects.last().title_name_russian
    email_1 = Info.objects.last().email_1
    email_2 = Info.objects.last().email_2
    phone_1 = Info.objects.last().phone_1
    phone_2 = Info.objects.last().phone_2
    address_1 = Info.objects.last().address_1
    address_2 = Info.objects.last().address_2
    address_1_russian = Info.objects.last().address_1_russian
    address_2_russian = Info.objects.last().address_2_russian
    work_hours = Info.objects.last().work_hours
    instagram_link = Info.objects.last().instagram_link
    tiktok_link = Info.objects.last().tiktok_link
    telegram_link = Info.objects.last().telegram_link

    current_url = request.get_full_path()
    if current_url == "/":
        turkmen_url = "/tm"
        russian_url = "/ru"
    else:
        turkmen_url = current_url.replace('ru', 'tm')
        russian_url = current_url.replace('tm', 'ru')
        
    cart_items_length = CartItem.objects.count()
    context = {
        'logo_name': logo_name,
        'title_name': title_name,
        'title_name_russian': title_name_russian,
        'email_1': email_1,
        'email_2': email_2,
        'phone_1': phone_1,
        'phone_2': phone_2,
        'address_1': address_1,
        'address_2': address_2,
        'address_1_russian': address_1_russian,
        'address_2_russian': address_2_russian,
        'work_hours': work_hours,
        'instagram_link': instagram_link,
        'tiktok_link': tiktok_link,
        'telegram_link': telegram_link,

        'current_url': current_url,
        'turkmen_url': turkmen_url,
        'russian_url': russian_url,

        'cart_items_length': cart_items_length
    }
    return context
