def context_data(request):
    from .models import Info
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
        'work_hours': work_hours
    }
    return context
