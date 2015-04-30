#coding=utf-8
from django.db import models
from wi_cache.base import CachingManager
from django.db.models import Max



class BoxType(object):
    NORMAL = 1
    HEADER_SHOW = 0
    TYPE_HASH = {
        NORMAL: u'普通盒子',
        HEADER_SHOW: u'轮播图'
    }
    
    TYPES = [
        (NORMAL, u'普通盒子'),
        (HEADER_SHOW, u'轮播图'),
    ]

    @classmethod
    def to_s(cls,itype):
        return TYPE_HASH.get(itype)


class Box(models.Model):

    title = models.CharField(max_length=100, default=u'标题')
    position = models.IntegerField(verbose_name=u'位置', default=0, db_index=True)


    state = models.IntegerField(verbose_name=u"状态(开/关)", choices=Status.STATUS, default=0, db_index=True, max_length=2)
    iner_count = models.IntegerField(verbose_name=u"内部容器个数", default=12)

    box_type = models.IntegerField(verbose_name=u"模块类型", choices=BoxType.TYPES,default=BoxType.NORMAL, db_index=True)

    created_at = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name=u'删除标记', default=False, db_index=True)

    box_id = models.ForeignKey(verbose_name=u'模块ID',HomeBox)
    objects = CachingManager()

    class Meta:
        verbose_name = u"首页盒子"
        verbose_name_plural = verbose_name
        app_label = "content"

    @property
    def box_type_to_s(self):
        box_type = BoxType.to_s(int(self.box_type))
        return box_type





