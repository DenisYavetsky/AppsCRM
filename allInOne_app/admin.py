from django.contrib import admin
from .models import *


# регистрируем модели
admin.site.register(ApplicationStatus)
admin.site.register(Application)
admin.site.register(ApplicationHistory)
admin.site.register(Service)
admin.site.register(PersonalGroup)
admin.site.register(Personal)