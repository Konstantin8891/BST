import datetime
import json

import xlsxwriter

from django.http import HttpResponse, FileResponse
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


def get_report(request):
    if request.method != 'GET':
        return HttpResponse('Method not allowed')
    date_now = datetime.datetime.now()
    first_day = date_now.date() - datetime.timedelta(days=date_now.weekday())
    robots = Robot.objects.filter(created__gte=first_day).order_by('serial')
    print(robots.all())
    data_for_table = dict()
    for robot in robots:
        if data_for_table.get(robot.model):
            if data_for_table.get(robot.version):
                data_for_table[robot.model][robot.version] += 1
            else:
                # data_for_table[robot.model] = dict()
                data_for_table[robot.model][robot.version] = 1
        else:
            data_for_table[robot.model] = dict()
            data_for_table[robot.model][robot.version] = 1
    print(data_for_table)
    workbook = xlsxwriter.Workbook('report.xlsx')
    for model, versions in data_for_table.items():
        print(model)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Модель')
        worksheet.write('B1', 'Версия')
        worksheet.write('C1', 'Количество за неделю')
        counter = 2
        print(versions)
        for version, amount in versions.items():
            worksheet.write(f'A{counter}', model)
            worksheet.write(f'B{counter}', version)
            worksheet.write(f'C{counter}', amount)
            counter += 1
    workbook.close()

    return FileResponse(open('report.xlsx', 'rb'))
