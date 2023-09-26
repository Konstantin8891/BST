import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from customers.models import Customer


@csrf_exempt
def add_order(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    data = json.loads(request.body)
    if not data.get('customer'):
        return HttpResponse('Customer not found')
    if not data.get('robot_serial'):
        return HttpResponse('Robot serial not found')
    customer = Customer.objects.filter(pk=data['customer']).first()
    if not customer:
        return HttpResponse('Incorrect customer')
    Order.objects.create(customer=customer, robot_serial=data['robot_serial'])
    return HttpResponse('Created')
