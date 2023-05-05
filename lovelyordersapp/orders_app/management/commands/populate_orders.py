from django.core.management.base import BaseCommand
from orders_app.utils import populate_orders

class Command(BaseCommand):
    help = 'Populate orders from the third-party API'

    def handle(self, *args, **options):
        populate_orders()
        self.stdout.write(self.style.SUCCESS('Orders populated successfully'))
