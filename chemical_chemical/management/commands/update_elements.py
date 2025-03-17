import csv
from django.core.management.base import BaseCommand
from chemical_chemical.models import Element

class Command(BaseCommand):
    help = 'Update elements in the database from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('elements_csv', type=str, help='The path to the elements CSV file')

    def handle(self, *args, **kwargs):
        elements_csv = kwargs['elements_csv']

        # Load elements dataset and update the database
        with open(elements_csv, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                element, created = Element.objects.update_or_create(
                    symbol=row['Symbol'],
                    defaults={
                        'name': row['Name'],
                        'atomic_number': row['Atomic_Number'],
                        'atomic_weight': row['Atomic_Weight'],
                        'density': row['Density'],
                        'melting_point': row['Melting_Point'],
                        'boiling_point': row['Boiling_Point'],
                        'phase': row['Phase'],
                        'group': row['Group'],
                        'period': row['Period'],
                        'category': row['Category']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created element {row['Name']} ({row['Symbol']})"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated element {row['Name']} ({row['Symbol']})"))

        self.stdout.write(self.style.SUCCESS('Successfully updated elements'))
