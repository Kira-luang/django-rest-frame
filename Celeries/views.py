from django.http import HttpResponse

from Celeries.tasks import add , send_email


def test(request):
    result = add(55 , 15)
    return HttpResponse(result)


def test_celery(request):
    result = add.delay(2 , 3)
    return HttpResponse(result)


def email(request):
    result = send_email.delay()
    return HttpResponse('请打开邮箱激活')
