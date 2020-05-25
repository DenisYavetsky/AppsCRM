from django.urls import path
from allInOne_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main_url'),
    path('alt/', views.new, name='new'),
    path('todo/', views.todolist, name='todolist'),
    path('application/', views.applicationList, name='applicationList'),
    path('application/add', views.applicationAdd, name='applicationAdd'),
    path('application/read/<int:pk>', views.applicationRead, name='applicationRead'),
    path('application/change/<int:pk>', views.applicationChange, name='applicationChange'),
    path('application/delete/<int:pk>', views.applicationDelete, name='applicationDelete'),
    path('applicationStatus/', views.applicationStatusList, name='applicationStatusList'),
    path('applicationStatus/add', views.applicationStatusAdd, name='applicationStatusAdd'),
    path('applicationStatus/change/<int:pk>', views.applicationStatusChange, name='applicationStatusChange'),
    path('applicationStatus/delete/<int:pk>', views.applicationStatusDelete, name='applicationStatusDelete'),
    path('service/', views.serviceList, name='serviceList'),
    path('service/add', views.serviceAdd, name='serviceAdd'),
    path('service/change/<int:pk>', views.serviceChange, name='serviceChange'),
    path('service/delete/<int:pk>', views.serviceDelete, name='serviceDelete'),
    path('personal/', views.personalList, name='personalList'),
    path('personal/add', views.personalAdd, name='personalAdd'),
    path('personal/change/<int:pk>', views.personalChange, name='personalChange'),
    path('personal/delete/<int:pk>', views.personalDelete, name='personalDelete'),
    path('personalgroup/', views.personalGroupList, name='personalGroupList'),
    path('personalgroup/add', views.personalGroupAdd, name='personalGroupAdd'),
    path('personalgroup/change/<int:pk>', views.personalGroupChange, name='personalGroupChange'),
    path('personalgroup/delete/<int:pk>', views.personalGroupDelete, name='personalGroupDelete'),
    path('customer/', views.customerList, name='customerList'),
    path('customer/add', views.customerAdd, name='customerAdd'),
    path('customer/change/<int:pk>', views.customerChange, name='customerChange'),
    path('customer/delete/<int:pk>', views.customerDelete, name='customerDelete'),
]
