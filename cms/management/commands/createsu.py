from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="XXX").exists():
            User.objects.create_superuser(username="XXX", email="YYY", password="ZZZ")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))