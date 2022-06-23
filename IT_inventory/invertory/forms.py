from django import forms
from .models import *
# from bootstrap_datepicker_plus import DatePickerInput
import bootstrap_datepicker_plus


class AddItActiveForm(forms.Form):
    title = forms.ModelChoiceField(empty_label='Выберите актив для ввода в эксплуатацию', queryset=Nomenclature.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    place = forms.ModelChoiceField(empty_label='Выберите аудиторию, где будет эксплуатироваться объект', queryset=Places.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    employee = forms.ModelChoiceField(empty_label='Выберите ответственного', queryset=Employees.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    # document = forms.ModelChoiceField(empty_label='Документ', queryset=Docs_type.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(empty_label='Статус оборудования', queryset=Statuses.objects.all(),
                                    label='Отметьте статус оборудования',
                                    widget=forms.Select(attrs={'class': 'form-control'}))


class UnregisterItActiveForm(forms.Form):
    title = forms.ModelChoiceField(empty_label='Выберите актив для снятия с учета',
                                   queryset=Nomenclature.objects.filter(place_id=11),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    # employee = forms.ModelChoiceField(empty_label='Выберите \'-\'', queryset=Employees.objects.get(name='-'),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    # document = forms.ModelChoiceField(empty_label='Документ', queryset=Docs_type.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    # status = forms.ModelChoiceField(empty_label='Выберите снять с учета', queryset=Statuses.objects.get(title='снят с учета'),
    #                                 label='Отметьте статус оборудования',
    #                                 widget=forms.Select(attrs={'class': 'form-control'}))


class RegisterItActiveForm(forms.Form):
    title = forms.CharField(max_length=150, label='Наименование сетевого оборудования',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')
    description = forms.CharField(max_length=1000, label='Описание', required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    employee = forms.ModelChoiceField(empty_label='МОЛ', queryset=Employees.objects.all(),
                                      label='Выберите материально ответственное лицо (МОЛ)',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(empty_label='Статус оборудования', queryset=Statuses.objects.exclude(title='снят с учета'),
                                       label='Отметьте статус оборудования',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    # document = forms.ModelChoiceField(empty_label='Документ', queryset=Docs_type.objects.all(),
    #                                 label='Выберите документ, на основании которого выполняется постановка на учет',
    #                                 widget=forms.Select(attrs={'class': 'form-control'}))


class DelItActiveForm(forms.Form):
    title = forms.ModelChoiceField(empty_label='Выберите актив для снятия с эксплуатации',
                                   queryset=Nomenclature.objects.exclude(place=Places.objects.get(title='склад')),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    employee = forms.ModelChoiceField(empty_label='МОЛ', queryset=Employees.objects.all(),
                                      label='Выберите материально ответственное лицо (МОЛ)',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(empty_label='Статус оборудования', queryset=Statuses.objects.all(),
                                       label='Отметьте статус оборудования',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    # document = forms.ModelChoiceField(empty_label='Документ', queryset=Docs_type.objects.all(),
    #                                 label='Выберите документ, на основании которого выполняется постановка на учет',
    #                                 widget=forms.Select(attrs={'class': 'form-control'}))


class CreateReport(forms.Form):
    filter_by_nomenclature = forms.ModelChoiceField(empty_label='По наименованию актива', queryset=Nomenclature.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    # filter_by_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')
    #
    # starting_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'}))
    # ending_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'}))

    # date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=BootstrapDateTimePickerInput())

    #
    filter_by_employee = forms.ModelChoiceField(empty_label='По сотруднику, за которым закреплен актив', queryset=Employees.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    filter_by_place = forms.ModelChoiceField(empty_label='По аудитории, в которой находится актив', queryset=Places.objects.all(),
                                       widget = forms.Select(attrs={'class': 'form-control'}), required=False)
    filter_by_status = forms.ModelChoiceField(empty_label='По техническому состоянию актива ', queryset=Statuses.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    filter_by_document = forms.ModelChoiceField(empty_label='По типу документа, на основании которого было выполнено последнее действие с активом', queryset=Docs_type.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}), required=False)

    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)