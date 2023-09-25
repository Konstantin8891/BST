import datetime
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


@csrf_exempt
def add_robot(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    # print(dir(request))
    data = json.loads(request.body)
    print(data)
    if not data.get('model'):
        return HttpResponse('No model in input data')
    if not data.get('version'):
        return HttpResponse('No version in input data')
    if not data.get('created'):
        return HttpResponse('No date in input data')
    try:
        datetime.datetime.strptime(data['created'], '%Y-%m-%d %H:%M:%S')
    except Exception:
        return HttpResponse('Incorrect date')
    Robot.objects.create(
        serial=data['model'] + '-' + data['version'],
        model=data['model'],
        version=data['version'],
        created=data['created']
    )
    return HttpResponse('Ok')
