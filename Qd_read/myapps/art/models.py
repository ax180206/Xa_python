import uuid

import os
from django.db import models

# Create your models here.
from django.utils import timezone

from DjangoUeditor.models import UEditorField


class Tag(models.Model):
#   name , decribe ,add_time
    name=models.CharField(max_length=20,verbose_name='标题')
    describe=models.CharField(max_length=255,verbose_name='描述')
    add_time=models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    def __str__(self):
        return self.name

    #   当前类表示对应表的信息
    class Meta:       # 元信息-描述模型类的信息（ORM）
        db_table='t_tag'    #类对应 数据库的表名
        verbose_name='标签'  #在后台显示模型类的名字
        verbose_name_plural=verbose_name  #后台复数的显示
        ordering=['-add_time']

class Category(models.Model):
    title=models.CharField(max_length=50,unique=True,verbose_name='标题')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    #父分类关系 ，未声明先引用：‘类名’或self
    parent=models.ForeignKey('self',verbose_name='所属分类',on_delete=models.SET_NULL,
                             blank=True,null=True) #blank在后台管理中是否可以为空，验证用


    def __str__(self):
        return self.title

    class Meta:
        db_table='t_category'
        verbose_name = '小说分类'  # 在后台显示模型类的名字
        verbose_name_plural = verbose_name  # 后台复数的显示

def new_file_name(instance,filname):
    new_name=str(uuid.uuid4())+os.path.splitext(filname)[-1]
    return 'arts/{}'.format(new_name)

class Art(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    summary=models.CharField(max_length=255,verbose_name='描述')
    contents=models.TextField(verbose_name='详细说明')
    author = models.CharField(max_length=20,verbose_name='作者')
    pulish_data=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    change_time=models.DateTimeField(auto_now=True,verbose_name='最近更新时间')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类名',default=1)
    tags= models.ManyToManyField(Tag,verbose_name='标签')
    #多对多默认自动建表，自定义的添加through ，并创建第三方表

    #文章的封面图片    依赖于pillow库
    img=models.ImageField(verbose_name='封面',upload_to=new_file_name,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='t_art'
        verbose_name = '小说'  # 在后台显示模型类的名字
        verbose_name_plural = verbose_name  # 后台复数的显示
        ordering=['-pulish_data']

class Rollset(models.Model):
    name=models.CharField(max_length=50,unique=True,verbose_name='名称')

    f_level=((0,'免费'),(1,'VIP'))
    free_level=models.IntegerField(verbose_name='免费级别',choices=f_level,default=0)
    art=models.ForeignKey(Art,on_delete=models.CASCADE,verbose_name='所属小说')
    @property
    def free_level_name(self):
        return self.f_level[self.free_level][1]

    def __str__(self):
        return self.name

    class Meta:
        db_table='t_roll'
        verbose_name='卷集'
        verbose_name_plural=verbose_name
        ordering=['id']

class Chapter(models.Model):
    name=models.CharField(max_length=50,verbose_name='章节名称')
    # content=models.TextField(verbose_name='文章内容')
    content = UEditorField(verbose_name="文章内容",
                 width=600, height=800,
                 imagePath="uediter/arts/images/",
                 blank=True,
                 toolbars="mini",
                 default='')
    #toolbars 富文本编辑框的工具栏 取值为：mini,normal,full，代表小，一般，全部
    pulish_time=models.DateTimeField(auto_now_add=True,verbose_name='发表时间')
    roll=models.ForeignKey(Rollset,on_delete=models.CASCADE,verbose_name='所属卷集')

    def __str__(self):
        return self.name

    class Meta:
        db_table='t_chapter'
        verbose_name='单章详情'
        verbose_name_plural=verbose_name
        ordering=['pulish_time']