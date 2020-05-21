from django.shortcuts import render
from .forms import ApplicationForm, ApplicationStatusForm, ServiceForm
from django.shortcuts import redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory, inlineformset_factory
from django.db.models import Avg, Max, Min


def main(request):
    return render(request, 'main.html', context={})


def new(request):
    return render(request, 'new.html', context={})


# заявки
def applicationList(request):
    application = Application.objects.all()

    return render(request, 'ApplicationList.html', context={'applications': application})


def applicationRead(request, pk):
    application = Application.objects.get(pk=pk)
    print(application)
    return render(request, 'applicationRead.html', {'application': application})


def applicationChange(request, pk):
    app = Application.objects.get(pk=pk)
    status = ApplicationStatus()
    print(app)
    # LanguageFormset = modelformset_factory(Language, fields=('name',))
    statFormset = inlineformset_factory(ApplicationStatus, Application, fields=('name',))
    print(statFormset)
    if request.method == 'POST':
        # formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = statFormset(request.POST, instance=app)
        if formset.is_valid():
            formset.save()
            # instances = formset.save(commit=False)
            # for instance in instances:
            #    instance.programmer_id = programmer.id
            #    instance.save()

            return redirect('applicationList', pk=app.id)

    # formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = statFormset(instance=status)
    print(formset)
    return render(request, 'applicationChange.html', {'formset': formset})


def applicationAdd(request):
    # application = Application()

    form = ApplicationForm()
    # application_form = inlineformset_factory(ApplicationStatus, Application, fields='__all__')
    if request.method == "POST":
        # читаем номер последний заявки
        number = Application.objects.all().aggregate(Max('number'))
        form = ApplicationForm(request.POST)
        if form.is_valid():
            App = form.save(commit=False)
            # номер новой заявки
            App.number = number['number__max'] + 1
            App.save()
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
