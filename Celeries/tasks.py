from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from django.http import BadHeaderError , HttpResponse

import os

# django环境初始化,wsgi.py里的代码复制过来
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "Django_rest_frame.settings")


@shared_task
def add(x , y):
    sleep(5)
    return x + y


@shared_task
def mul(x , y):
    sleep(5)
    return x * y


@shared_task
def send_email():
    subject = 'Test,这是再修改后的'  # 邮件标题
    message = 'Hello,这是异步发的'  # 文档
    from_email = 'kira_luang@163.com'  # 邮件来源地址
    recipient_list = ['2920167524@qq.com' , ]  # 接收邮件地址
    send_mail(subject , message , from_email , recipient_list=recipient_list)
