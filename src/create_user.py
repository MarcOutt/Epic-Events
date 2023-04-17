import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
django.setup()

from user.models import CustomUser

CustomUser.objects.create_user(email='r.lapierre@example.com',
                               first_name='Robert',
                               last_name='Lapierre',
                               role='management',
                               password='test_password')

CustomUser.objects.create_user(email='p.delacour@example.com',
                               first_name='Paul',
                               last_name='Delacour',
                               role='sale',
                               password='test_password')

CustomUser.objects.create_user(email='p.laroche@example.com',
                               first_name='Paul',
                               last_name='Laroche',
                               role='support',
                               password='test_password')
