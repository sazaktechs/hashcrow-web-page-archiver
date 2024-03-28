''' Configuring applications '''
from django.apps import AppConfig


class ApiConfig(AppConfig):
    ''' To configure an application, create an apps.py module inside the application, 
    then define a subclass of AppConfig there. '''
    name = 'api'
