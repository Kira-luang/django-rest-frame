# 什么是CBV
'''
CBV: Class/Browser/Views
'''

# CBV用法
'''
views定义:
class Books(View):
    def get(self, request, **kwargs):
        pass
    def post(self, request, **kwargs):
        pass
urls设置:
urlpatterns = [
    path('books/' , views.Books.as_view(), name='books') ,
]

只有定义了的方法能用,没有定义就不能使用
坑点:post方法暂时过不了csrf,而且urls一定是/结尾,要不然会报错
'''
