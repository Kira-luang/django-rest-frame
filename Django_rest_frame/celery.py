import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Django_rest_frame.settings')

app = Celery('Django_rest_frame')

app.config_from_object('django.conf:settings' , namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
