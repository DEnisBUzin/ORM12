import json
 
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']

        with open(json_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)

        for item in dct:
            b = Book(
                name=item['fields']['name'],
                author=item['fields']['author'],
                pub_date=item['fields']['pub_date'],
            )

            b.save()

