from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        User=get_user_model()
        u,_=User.objects.get_or_create(username="admin")
        u.set_password("admin123"); u.is_staff=True; u.is_superuser=True; u.save()
        self.stdout.write(self.style.SUCCESS("Admin ready: admin / admin123"))
