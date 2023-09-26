import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Customer


@csrf_exempt
def add_customer(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    data = json.loads(request.body)
    if not data.get('email'):
        return HttpResponse('Email not found')
    Customer.objects.create(email=data['email'])
    return HttpResponse('Created')
