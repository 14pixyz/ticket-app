from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from ticket.models import Company
import getpass

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Companyを作成
        company = Company.objects.create(
            name='test',
            adress='test',
            tel='00000000000'
        )
        print("Company作成")

        # スーパーユーザーを作成
        email = input("Superuser email: ")
        password = getpass.getpass("Superuser password: ")

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password=password,
                company=company
            )
            print("スーパーユーザー作成")
        else:
            print("スーパーユーザーは既に存在します")