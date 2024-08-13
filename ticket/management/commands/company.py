from django.core.management.base import BaseCommand
from ticket.models import Company

class Command(BaseCommand):
    def handle(self, *args, **options):
        Company.objects.create(
            name='test',
            adress='test',
            tel='00000000000'
        )
        print("company作成")

