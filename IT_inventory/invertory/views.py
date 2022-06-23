import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import operator
from django.db.models import Q
from functools import reduce

from .models import Nomenclature
from .forms import *

# Create your views here.

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    data = Nomenclature_Report.objects.all().values()

    writer.writerow(['Title', 'Price', 'Description'])
    for record in data:
        print(record)
        print('------')
        table = [record['title'], record['price'], record['description']]
        # for user in users:
        writer.writerow(table)

    data_to_del = Nomenclature_Report.objects.all()
    data_to_del.delete()
    return response


def index(request):
    nomenclature = Nomenclature.objects.all()
    return render(request, 'invertory/index.html', {'nomenclature': nomenclature, 'title' : 'Список оборудования'})

def it_actives(request):
    return render(request, 'invertory/it_actives.html')

def register_it_active(request):
    if request.method == 'POST':
        form = RegisterItActiveForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_to_nomen = Nomenclature(title=data['title'], price=data['price'], description=data['description'],
                                        status=data['status'], place=Places.objects.get(title='склад'))
            record_to_nomen.save()
            record_to_reg = Registry(document=Docs_type.objects.get(title='Приходная накладная'), employee=data['employee'], nomenclature=Nomenclature.objects.get(title=data['title']))
            record_to_reg.save()
            return redirect('success')
    else:
        form = RegisterItActiveForm()
    return render(request, 'invertory/register_it_active.html', {'form' : form})


def del_it_active(request):
    if request.method == 'POST':
        form = DelItActiveForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_to_reg = Registry(document=Docs_type.objects.get(title='Акт приема-передачи'), nomenclature=data['title'], employee=data['employee'])
            record_to_reg.save()
            nomenclature = Nomenclature.objects.get(title=data['title'])
            nomenclature.place = Places.objects.get(title='склад') # change field
            nomenclature.status = data['status'] # change field
            nomenclature.save()  # this will update only
            return redirect('success')
    else:
        form = DelItActiveForm()
    return render(request, 'invertory/del_it_active.html', {'form' : form})

def add_it_active(request):
    if request.method == 'POST':
        form = AddItActiveForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_to_reg = Registry(document=Docs_type.objects.get(title='Акт приема-передачи'), employee=data['employee'], nomenclature=data['title'])
            record_to_reg.save()
            nomenclature = Nomenclature.objects.get(title=data['title'])
            nomenclature.place = data['place']  # change field
            nomenclature.status = data['status']  # change field
            nomenclature.save()  # this will update only
            return redirect('success')
    else:
        form = AddItActiveForm()
    return render(request, 'invertory/add_it_active.html', {'form' : form})


def unregister_it_active(request):
    if request.method == 'POST':
        form = UnregisterItActiveForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_to_reg = Registry(document=Docs_type.objects.get(title='Документ об откреплении'), nomenclature=data['title'], employee=Employees.objects.get(name='-'))
            record_to_reg.save()
            nomenclature = Nomenclature.objects.get(title=data['title'])
            nomenclature.place = Places.objects.get(title='-')  # change field ??? should be zero or whatever
            nomenclature.status = Statuses.objects.get(title='снят с учета') # change field
            nomenclature.save()  # this will update only
            return redirect('success')
    else:
        form = UnregisterItActiveForm()
    return render(request, 'invertory/unregister_it_active.html', {'form' : form})


def create_report(request):
    if request.method == 'POST':
        form = CreateReport(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if (data['filter_by_nomenclature'] == None):
                qs1 = Nomenclature.objects.all()
            else:
                qs1 = Nomenclature.objects.filter(title=data['filter_by_nomenclature'])
            if (data['filter_by_place'] == None):
                qs2 = Nomenclature.objects.all()
            else:
                qs2 = Nomenclature.objects.filter(place=data['filter_by_place'])
            if (data['filter_by_status'] == None):
                qs3 = Nomenclature.objects.all()
            else:
                qs3 = Nomenclature.objects.filter(status=data['filter_by_status'])
            QS1 = qs1.intersection(qs2, qs3)

            if (data['filter_by_employee'] == None):
                qs1 = Nomenclature.objects.all()
            else:
                qs1 = Nomenclature.objects.filter(registry__employee=data['filter_by_employee']).distinct()
            if (data['filter_by_document'] == None):
                qs2 = Nomenclature.objects.all()
            else:
                qs2 = Nomenclature.objects.filter(registry__document=data['filter_by_document']).distinct()
            QS2 = qs1.intersection(qs2)

            if (data['start_date'] == None and data['end_date'] == None):
                QS3 = Nomenclature.objects.all()
            else:
                QS3 = Nomenclature.objects.filter(registry__registration_date__range=[data['start_date'],data['end_date']]).distinct()

            nomenclature = QS1.intersection(QS2, QS3).values()

            data_to_del = Nomenclature_Report.objects.all()
            data_to_del.delete()
            for record in nomenclature:
                Nomenclature_Report.objects.create(**record)
            # print(nomenclature)
            nomenclature_len = len(nomenclature)
            # return redirect('success')
    else:
        form = CreateReport()
        nomenclature_len = None
    return render(request, 'invertory/create_report.html', {'form' : form, 'nomenclature_len' : nomenclature_len})

def success(request):
    return render(request, 'invertory/success.html')

def developer_info(request):
    return render(request, 'invertory/developer_info.html')