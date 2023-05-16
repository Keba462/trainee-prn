from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'trainee_prn'
    verbose_name = 'Trainee PRN'
    admin_site_name = 'trainee_prn_admin'