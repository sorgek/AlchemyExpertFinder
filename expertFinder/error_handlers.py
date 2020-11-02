from django import http
from django.conf import settings

def bad_request(request, *args, **kwargs):
    return http.HttpResponseBadRequest(
        '<h1>Bad Request (400), DEUBG DATA: {}</h1>'.format(settings.ALLOWED_HOSTS),
        content_type='text/html')