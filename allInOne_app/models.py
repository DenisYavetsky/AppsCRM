from django.db import models


# статусы заявок
class ApplicationStatus(models.Model):
    # название статуса: создана, принята и т.д.
    name = models.CharField(max_length=100, blank=False, unique=True)
    # описание
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'

    def __str__(self):
        return '{}'.format(self.name)


# заявки
class Application(models.Model):
    # статус
    status = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)
    # дата создания
    date_create = models.DateTimeField(auto_now_add=True)
    # Не нужно возможно
    name = models.CharField(max_length=100)
    # номер заявки. Не привязан к ID
    number = models.IntegerField(default=0)

    # исполнитель
    # заказчик
    # услуга
    # стоимость
    # тип оплаты
    # примечание

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return '{}'.format(self.name)


# история заявки
class ApplicationHistory(models.Model):
    # ссылка на заявку
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE)
    # дата и время изменения
    date_change = models.DateTimeField(auto_now_add=True)
    # текст
    note = models.TextField(max_length=200, blank=False)

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'История заявки'
        verbose_name_plural = 'История заявок'

    def __str__(self):
        return '{}'.format(self.note)


# услуги
class Service(models.Model):
    # наименование
    name = models.CharField(max_length=150)
    # цена
    price = models.IntegerField(default=0)

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '{}'.format(self.name)


# группы сотрудников
class PersonalGroup(models.Model):
    # имя группы
    name = models.CharField(max_length=150)
    # описание
    description = models.TextField(max_length=150)

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'Группа пользователя'
        verbose_name_plural = 'Группы пользователей'

    def __str__(self):
        return '{}'.format(self.name)


# сотрудника
class Personal(models.Model):
    # имя сотрудника
    name = models.CharField(max_length=150)
    # описание
    group = models.ForeignKey(PersonalGroup, on_delete=models.CASCADE)

    class Meta:
        # единственное и множественное число модели в админке
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '{}'.format(self.name)
