from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('it_actives', it_actives, name='it_actives'),
    path('register_it_active', register_it_active, name='register_it_active'),
    path('add_it_active', add_it_active, name='add_it_active'),
    path('del_it_active', del_it_active, name='del_it_active'),
    path('unregister_it_active', unregister_it_active, name='unregister_it_active'),
    path('create_report', create_report, name='create_report'),
    path('success', success, name='success'),
    path('developer_info', developer_info, name='developer_info'),
    path('export_data', export_data, name='export_data')
]