# 系统（内置）模块
# 第三方的库
# 自己写的模块

import xadmin
from xadmin import views
from art.models import *


# Register your models here.
# 设置admin站点的样式


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    # 整体配置
    site_title = '新意小说'
    site_footer = 'Optimism胜 by Chens<br><h5 style="color:blue;font:华文行楷">倾尽时光暖流年</h5>'
    # menu_style = 'accordion'  # 菜单折叠
    # globals_search_model=[Tag]
    apps_label_title = {
        'art': '文章管理'
    }


xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)


class TagAdmin:
    list_display = ('name', 'describe', 'add_time')  # 列表展示字段
    search_fields = ('name', 'describe')  # 搜索字段
    list_filter=('add_time','name')   #过滤器
    list_per_page = 10  # 每页显示的记录数

class CategoryAdmin:
    list_display=('title','add_time')
    search_fields = ('title')  # 搜索字段
    list_filter=('add_time','title')   #过滤器
    list_per_page=10

class ArtAdmin:
    list_display=('title','summary','author','pulish_data','contents')
    list_per_page=10

class RollsetAdmin:
    list_display=('name','free_level','art')
    list_per_page=10

class ChapterAdmin:
    list_display=('name','pulish_time','roll')
    list_per_page=10

    style_fields = {'content': 'ueditor'}


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Art, ArtAdmin)
xadmin.site.register(Rollset,RollsetAdmin)
xadmin.site.register(Chapter,ChapterAdmin)