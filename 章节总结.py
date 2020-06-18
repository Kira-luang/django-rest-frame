# Views的CBV继承使用
'''
ListCreateAPIView: GET objects -> 查询一个集合
CreateAPIView：create object -> 创建一个记录
RetrieveAPIView: GET a object -> 查询一个记录
UpdateAPIView: Update a object -> 更新一个记录
DestroyAPIView: Delete a object -> 删除某个记录

各种基于以上功能组合而成的类
'''

# APIViews的原理
'''
利用GenericAPIView与各种mixins混合
GenericAPIView: 是一个工具箱
mixins: 操作CRUD
'''
