import xml.etree.ElementTree as ET

import os

from django.apps import apps

App = apps.get_model('apps','App')

'''
Loading the required model from the apps. Arguement f in parse_xml 
function is file path. I load the first module child of modules tag
which has the required info about the sift app like name, title
type.
'''

def parse_xml(f=None):
    app_dict = {}
    f = os.path.join(os.getcwd(), f)
    tree = ET.parse(f)
    module = tree.find('modules/module')
    app_dict['name'] = module.get('name')
    app_dict['title'] = module.get('name')
    app_dict['min_version'] = module.get('min_version')
    app_dict['type'] = module.get('type')

    app_type = 'M' if app_dict['type'] == 'ns-contrib' else 'F' 
    app_from_bake = App.objects.create(name=app_dict['name'],
                       title=app_dict['title'],
                       app_type=app_type,
                       abstract='App created from bake file',
                       description='App created from bake file')

