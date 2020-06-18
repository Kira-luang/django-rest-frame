# 用户登陆验证
"""测试时候记得打开redis"""
from Authentication.APISettings import UserPermission , UserAuthentication

'''
1.搭建基本框架
models -> 建表
serializers -> 序列化
urls -> 创建路由
views -> 请求处理

2.注册与登陆
由于两者都是利用POST的请求,所以要通过请求的参数action来实现判断
http://127.0.0.1:8000/authentication/users/?action=login

3.登陆Token
在登陆方法创建Token,在缓存中进行存储,再返回客户端

4.登陆验证
token的话需要重写一个继承自BaseAuthentication的类
中间可以添加验证
最后要返回类实例和token,具体操作看APISettings
authentication_classes = () -> 添加所写的Authentication类
Tip:Authentication类执行后会给request添加属性user和token,默认会作用全部的method
'''
具体参考 = UserAuthentication
# 用户权限验证
'''
1.创建类UserPermission,继承自BasePermission
重铸方法:has_permission,增加验证条件即可
'''
具体参考 = UserPermission
'''
2.Views里面的类添加设置
permission_classes = (UserPermission, )
'''
