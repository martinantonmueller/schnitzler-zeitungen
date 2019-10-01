from django.conf import settings
from . utils import SHARED_URL
from . utils import PROJECT_METADATA as PM


def my_app_name(request):
    return {'PROJECT_NAME': PM['title']}


def shared_url(request):
    return {'SHARED_URL': SHARED_URL}


def installed_apps(request):
    return {'APPS': settings.INSTALLED_APPS}


def is_dev_version(request):
    try:
        return {'DEV_VERSION': settings.DEV_VERSION}
    except AttributeError:
        return {}


def get_db_name(request):
    try:
        db_name = settings.DATABASES['default']['NAME']
        return {'DB_NAME': db_name}
    except Exception as e:
        return {}
