from django.core.management.base import BaseCommand, CommandError

from util.parse_bake import parse_xml

'''
importing parse_bake module from util directory. It has helper function
parse_xml which parses the xml file given in the path arguement ie
python manage.py saveapp [ path to xml ]
you can pass [ path to xml ] = util/sift.xml for this setup from django
root directory
'''
class Command(BaseCommand):
    help = 'Create new app from bake file'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+',type=str)

    def handle(self, *args, **options):
        for path in options['path']:
            try:
                parse_xml(path)
                print 'App created'
            except Exception as e :
                raise CommandError(e)