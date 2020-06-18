from django.http import HttpResponse , JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from CBV.models import Book


class Books(View):
    id = None

    def get(self , request , **kwargs):
        if kwargs:
            return self.get_id(request , **kwargs)
        book_all = Book.objects.all()
        book_list = []
        for book in book_all:
            book_list.append(book.get_dict())
        data = {
            'status': 200 ,
            'msg': '正常返回' ,
            'book': book_list
        }
        return JsonResponse(data)

    def post(self , request):
        csrf_exempt(self.post)
        book = Book.objects.create(name=request.POST.get('name') , price=request.POST.get('price'))
        data = {
            'status': 201 ,
            'msg': '正常返回' ,
            'book': book.get_dict()
        }
        return JsonResponse(data)

    def get_id(self , request , **kwargs):
        if request.method == 'GET':
            book = Book.objects.get(id=kwargs['id'])
            data = {
                'status': 200 ,
                'msg': 'get success' ,
                'data': book.get_dict()
            }
            return JsonResponse(data)

    def delete(self , request , **kwargs):
        book = Book.objects.get(id=kwargs['id'])
        book.delete()
        data = {
            'status': 204 ,
            'msg': 'delete success' ,
            # 'data': {}
        }
        return JsonResponse(data)
