'''本章主要内容是级联查询和节流'''

# 1.级联查询
'''
class UserSerializer(serializers.ModelSerializer):
    address_set = AddressSerializer(many=True , read_only=True)
    class Meta:
        model = User
        fields = ['username' , 'id' , 'password', 'address_set']
主表添加address_set的属性,并且添加到fields上显示
可参考官方文档:https://www.django-rest-framework.org/api-guide/relations/
'''

# 2.节流
'''
1.创建Throttle

class AddressRateThrottle(UserRateThrottle):  # 继承自UserRateThrottle
    scope = 'address'  # 取名

    def get_cache_key(self, request, view):  # 重写get_cache_key方法
        if isinstance(request.user, User):
            ident = request.auth  # 把token作为ident(令牌)
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
        
2.配置settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'App.Throttles.UserThrottle',  # 注册UserThrottle
        'App.Throttles.AddressRateThrottle',  # 注册AddressRateThrottle
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/min',  # 设置UserThrottle的频率
        'address': '10/m'  # 设置注册AddressRateThrottle的频率
    }
}

3.View添加频率类
throttle_classes = [UserThrottle, ]  # 添加UserThrottle的频率设置
'''
