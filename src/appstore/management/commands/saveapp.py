from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import Contributors Data'

    # CONTRIBUTORS = staticmethod(get_contrib_data)
    # IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
    	print('This is awesome')
        # CONTRIBUTORS_DATA = self.CONTRIBUTORS()
        # if CONTRIBUTORS_DATA:
        #     for contributor in CONTRIBUTORS_DATA:
        #         self.IMPORT_DATA(contributor)