# HyperlinkedModelSerializer的使用
'''
超链接模型解析
Serializers: 使用的是HyperlinkedModelSerializer
能够展现超链接,适用于自行使用,开发环境很少使用
Views:
Views: 使用的是viewsets.ModelViewSet
能够响应全部的请求
Urls:
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

path('' , include(router.urls))

坑点:只能配合这种Urls的注册方式来使用
'''

# HyperlinkedModelSerializer使用范例:
'''
views.py:
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
创建serializer.py:
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

urls:
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

path('' , include(router.urls))
'''
