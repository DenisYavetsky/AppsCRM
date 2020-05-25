from django.shortcuts import render
from .forms import ApplicationForm, ApplicationStatusForm, ServiceForm, PersonalGroupForm, PersonalForm, CustomerForm
from django.shortcuts import redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory, inlineformset_factory
from django.db.models import Avg, Max, Min


def main(request):
    # добавить заяку
    data = dict()
    data['method'] = 'add'

    form = ApplicationForm()
    # application_form = inlineformset_factory(ApplicationStatus, Application, fields='__all__')
    if request.method == "POST":
        # читаем номер последний заявки
        number = Application.objects.all().aggregate(Max('number'))
        form = ApplicationForm(request.POST)

        if form.is_valid():

            App = form.save(commit=False)

            # номер новой заявки
            if str(number['number__max']) == 'None':
                App.number = 1
            else:
                App.number = number['number__max'] + 1
            #App.customer = Customer.objects.get(name="Тестовый заказчик")

            App.save()

            application_history_add(App, data)
            return redirect('applicationList')
        else:
            form = ApplicationForm()

    return render(request, 'landing.html', {'form': form})


def todolist(request):
    return render(request, 'todolist.html', context={})


def new(request):
    return render(request, 'LeftMenu.html', context={})


# заявки
def applicationList(request):
    application = Application.objects.all()
    return render(request, 'ApplicationList.html', context={'applications': application})


def applicationRead(request, pk):
    application = Application.objects.get(pk=pk)
    applicationhistories = ApplicationHistory.objects.filter(application_id=application)
    print(applicationhistories)
    return render(request, 'applicationRead.html',
                  {'application': application, 'applicationhistories': applicationhistories})


def applicationChange(request, pk):
    data = dict()
    data['method'] = 'change'

    application = get_object_or_404(Application, pk=pk)
    # запоминаем что было до именения заявки
    data['status'] = application.status
    data['name'] = application.name
    data['service'] = application.service
    form_c = CustomerForm()
    form = ApplicationForm(instance=application)
    if request.method == "POST":

        form = ApplicationForm(request.POST, instance=application)

        if form.is_valid():

            application = form.save(commit=False)
            application.save()

            application_history_add(application, data)

            return redirect('applicationList')
        else:
            form = ApplicationForm(instance=application)

    return render(request, 'applicationChange.html', context={'application': application, 'form': form, 'form_c': form_c})


def applicationAdd(request):
    # добавить заяку
    data = dict()
    data['method'] = 'add'

    form = ApplicationForm()
    # application_form = inlineformset_factory(ApplicationStatus, Application, fields='__all__')
    if request.method == "POST":
        # читаем номер последний заявки
        number = Application.objects.all().aggregate(Max('number'))
        form = ApplicationForm(request.POST)
        if form.is_valid():
            App = form.save(commit=False)
            # номер новой заявки
            if str(number['number__max']) == 'None':
                App.number = 1
            else:
                App.number = number['number__max'] + 1
            App.save()

            application_history_add(App, data)
            return redirect('applicationList')
        else:
            form = ApplicationForm()

    return render(request, 'applicationAdd.html', {'form': form})


def applicationDelete(request, pk):
    status = get_object_or_404(ApplicationStatus, pk=pk)
    if request.method == "POST":
        status.delete()
        return redirect('applicationList')
    return render(request, 'ApplicationDelete.html', context={'status': status})


# Статусы заявок
def applicationStatusList(request):
    AppStatus = ApplicationStatus.objects.all()
    return render(request, 'ApplicationStatusList.html', context={'AppStatus': AppStatus})


def applicationStatusAdd(request):
    if request.method == "POST":
        form = ApplicationStatusForm(request.POST)
        if form.is_valid():
            ApplicationStatus = form.save(commit=False)
            ApplicationStatus.save()
            return redirect('applicationStatusList')
        else:
            form = ApplicationStatusForm()
    return render(request, 'ApplicationStatusAdd.html', context={})


def applicationStatusDelete(request, pk):
    status = get_object_or_404(ApplicationStatus, pk=pk)
    if request.method == "POST":
        status.delete()
        return redirect('applicationStatusList')
    return render(request, 'ApplicationStatusDelete.html', context={'status': status})


def applicationStatusChange(request, pk):
    status = get_object_or_404(ApplicationStatus, pk=pk)
    form = ApplicationStatusForm(instance=status)
    if request.method == "POST":
        form = ApplicationStatusForm(request.POST, instance=status)
        if form.is_valid():
            status = form.save(commit=False)
            status.save()
            return redirect('applicationStatusList')
        else:
            form = ApplicationStatusForm(instance=status)

    return render(request, 'ApplicationStatusChange.html', context={'status': status})


def applicationStatus(request):
    if request.method == "POST":
        form = ApplicationStatusForm(request.POST)
        if form.is_valid():
            ApplicationStatus = form.save(commit=False)
            ApplicationStatus.save()
            return redirect('main_url')
    else:
        form = ApplicationStatusForm()
    return render(request, 'ApplicationStatusList.html', {'form': form})


# Список услуг
def serviceList(request):
    services = Service.objects.all()
    return render(request, 'ServiceList.html', context={'services': services})


def serviceAdd(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('serviceList')
        else:
            form = ServiceForm()
    return render(request, 'ServiceAdd.html', context={})


def serviceChange(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(instance=service)
    if request.method == "POST":

        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():

            service = form.save(commit=False)
            service.save()
            return redirect('serviceList')
        else:
            form = ServiceForm(instance=service)

    return render(request, 'ServiceChange.html', context={'service': service})


def serviceDelete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        return redirect('serviceList')
    return render(request, 'ServiceDelete.html', context={'service': service})


# Список услуг
def personalList(request):
    personals = Personal.objects.all()
    return render(request, 'PersonalList.html', context={'personals': personals})


def personalAdd(request):
    # application = Application()

    form = PersonalForm()

    if request.method == "POST":

        form = PersonalForm(request.POST)
        if form.is_valid():
            Per = form.save(commit=False)

            Per.save()
            return redirect('personalList')
        else:
            form = PersonalForm()

    return render(request, 'personalAdd.html', {'form': form})


def personalChange(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    form = PersonalForm(instance=personal)
    if request.method == "POST":

        form = PersonalForm(request.POST, instance=personal)

        if form.is_valid():

            personal = form.save(commit=False)
            personal.save()
            return redirect('personalList')
        else:
            form = PersonalForm(instance=personal)

    return render(request, 'personalChange.html', context={'personal': personal, 'form': form})


def personalDelete(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        personal.delete()
        return redirect('personalList')
    return render(request, 'PersonalDelete.html', context={'personal': personal})


# Список услуг
def personalGroupList(request):
    personalGroups = PersonalGroup.objects.all()
    return render(request, 'PersonalGroupList.html', context={'personalGroups': personalGroups})


def personalGroupAdd(request):
    if request.method == "POST":
        form = PersonalGroupForm(request.POST)
        if form.is_valid():
            personalGroup = form.save(commit=False)
            personalGroup.save()
            return redirect('personalGroupList')
        else:
            form = PersonalGroupForm()
    return render(request, 'PersonalGroupAdd.html', context={})


def personalGroupChange(request, pk):
    personalGroup = get_object_or_404(PersonalGroup, pk=pk)
    form = PersonalGroupForm(instance=personalGroup)
    if request.method == "POST":

        form = PersonalGroupForm(request.POST, instance=personalGroup)

        if form.is_valid():

            personalGroup = form.save(commit=False)
            personalGroup.save()
            return redirect('personalGroupList')
        else:
            form = PersonalGroupForm(instance=personalGroup)

    return render(request, 'personalGroupChange.html', context={'personalGroup': personalGroup})


def personalGroupDelete(request, pk):
    personalGroup = get_object_or_404(PersonalGroup, pk=pk)
    if request.method == "POST":
        personalGroup.delete()
        return redirect('personalGroupList')
    return render(request, 'PersonalGroupDelete.html', context={'personalGroup': personalGroup})


# Список заказчиков
def customerList(request):
    customers = Customer.objects.all()
    return render(request, 'CustomerList.html', context={'customers': customers})


def customerAdd(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customerList')
        else:
            form = CustomerForm()
    return render(request, 'CustomerAdd.html', context={})


def customerChange(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":

        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():

            customer = form.save(commit=False)
            customer.save()
            return redirect('customerList')
        else:
            form = CustomerForm(instance=customer)

    return render(request, 'CustomerChange.html', context={'customer': customer})


def customerDelete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customerList')
    return render(request, 'customerDelete.html', context={'customer': customer})


def application_history_add(application, data):
    if data['method'] == 'add':
        h = ApplicationHistory()
        h.note = 'Заявка создана'
        h.application_id = application
        h.save()
    if data['method'] == 'change':
        if data['name'] != application.name:
            h = ApplicationHistory()
            h.note = 'Имя заявки "' + data['name'] + '" изменено на "' + application.name + '"'
            h.application_id = application
            h.save()
        if data['service'] != application.service:
            h = ApplicationHistory()
            h.note = 'Услуга заявки "' + data['service'] + '" изменена на "' + application.service + '"'
            h.application_id = application
            h.save()
        if data['status'] != application.status:
            print(data['status'], application.status)
            h = ApplicationHistory()
            h.note = 'Статус заявки ' + str(data['status']) + ' изменен на ' + str(application.status)
            h.application_id = application
            h.save()
