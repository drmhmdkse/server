import os
import  random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restpro.settings')


import django
django.setup()

from django.contrib.auth.models import User

from faker import Faker

def set_user():
    fake=Faker(['en-US'])
    first_name=fake.first_name()
    last_name=fake.last_name()
    username=f'{first_name.lower()}_{last_name.lower()}'
    email=f'{username}@hotmail.com'

    user_check=User.objects.filter(username=username)
    while user_check.exists():
        username=username+str(random.randint(1,99))
        user_check = User.objects.filter(username=username)


    user=User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    user.set_password("Kose.1965")
    user.save()