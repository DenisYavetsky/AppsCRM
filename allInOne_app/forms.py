from django import forms
from .models import Application, ApplicationStatus, Service
from django.forms import inlineformset_factory


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
        fields = ('name', 'status')
        # псевдонимы полей для заполнения
        labels = {'name': 'Название заявки',
                  'status': 'Статус заявки'}

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
