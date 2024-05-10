from django.dispatch import Signal



def get_client_ip(request):
    x_forwarded_for = request.META.get('X_FORWADED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip