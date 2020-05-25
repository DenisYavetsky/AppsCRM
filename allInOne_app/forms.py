from django import forms
from .models import Application, ApplicationStatus, Service, PersonalGroup, Personal, Customer
from django.forms import inlineformset_factory


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # поля для заполнения
        fields = ('fio', 'phone', 'email')
        # псевдонимы полей для заполнения
        labels = {'fio': 'Имя',
                  'phone': 'Телефон',
                  'email': 'Почта'}

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['fio'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # поля для заполнения
        fields = ('name', 'price')
        # псевдонимы полей для заполнения
        labels = {'name': 'Название услуги',
                  'price': 'Цена услуги'}


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = ApplicationStatus
        # поля для заполнения
        fields = ('name', 'description')
        # псевдонимы полей для заполнения
        labels = {'name': 'Название статуса заявки',
                  'description': 'Описание статуса заявки'}


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        # поля для заполнения
        fields = ('name', 'status', 'service', 'prim', 'customer', 'worker', 'operator')
        # псевдонимы полей для заполнения
        labels = {'name': 'Название заявки',
                  'status': 'Статус заявки',
                  'service': 'Услуга',
                  'prim': 'Примечание'}

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['worker'].queryset = Personal.objects.filter(group=2)
        self.fields['operator'].queryset = Personal.objects.filter(group=1)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['customer'].widget.attrs.update({'class': 'form-control'})
        self.fields['worker'].widget.attrs.update({'class': 'form-control'})
        self.fields['operator'].widget.attrs.update({'class': 'form-control'})


class PersonalGroupForm(forms.ModelForm):
    class Meta:
        model = PersonalGroup
        # поля для заполнения
        fields = ('name', 'description')
        # псевдонимы полей для заполнения
        labels = {'name': 'Название группы пользователей',
                  'description': 'Описание группы пользователей'}


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        # поля для заполнения
        fields = ('name', 'group')
        # псевдонимы полей для заполнения
        labels = {'name': 'Имя пользователя',
                  'group': 'Группа пользователя'}

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['group'].widget.attrs.update({'class': 'form-control'})
