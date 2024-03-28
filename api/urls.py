'''
Django Urls
'''
from django.urls import path
from . import views

urlpatterns = [
    path('hashurl/', views.hashurl),
    path('check/',views.check_version_is_up_to_date),
    path('list/',views.snapshot_info),
    path('listpages/', views.listpages),
]
