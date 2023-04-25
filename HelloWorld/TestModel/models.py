# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from datetime import datetime



class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_sex = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=11)
    avatar = models.CharField(max_length=6, blank=True, null=True)
    superuser = models.IntegerField(blank=True, null=True)
    last_login_time = models.DateTimeField('最后修改日期', auto_now = True,blank=True, null=True)
    register_time = models.DateTimeField('注册日期',blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'USER'

class BlogType(models.Model):
    type_id = models.AutoField(primary_key=True) #, db_comment='类型id'
    type_name = models.CharField(max_length=32)#, db_comment='类型名称'

    class Meta:
        managed = False
        db_table = 'blog_type'


class TBlog(models.Model):
    blog_id = models.BigAutoField(primary_key=True) #, db_comment='博客id'
    blog_title = models.CharField(max_length=100)#, db_comment='博客标题'
    blog_content = models.TextField()#db_comment='博客内容'
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='id', blank=True, null=True)#, db_comment='创建人id'
    type = models.ForeignKey(BlogType, models.DO_NOTHING, blank=True, null=True)#, db_comment='类型id'
    blog_status = models.IntegerField()#db_comment='博客状态 1为发布 0为草稿'
    create_time = models.DateTimeField()#db_comment='创建时间'
    update_time = models.DateTimeField()#db_comment='更新时间'
    cover_image = models.CharField(max_length=255, blank=True, null=True)#, db_comment='封面图片'

    class Meta:
        managed = False
        db_table = 't_blog'


class TComment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)#, db_comment='评论id'
    comment_content = models.CharField(max_length=500)#, db_comment='评论内容'
    blog = models.ForeignKey(TBlog, models.DO_NOTHING)#, db_comment='评论内容'
    createtime = models.DateTimeField()#db_comment='评论时间'
    id = models.ForeignKey(User, models.DO_NOTHING)#, db_comment='评论人ID'
    replyid = models.IntegerField()#db_comment='评论回复人ID'

    class Meta:
        managed = False
        db_table = 't_comment'


class TTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 't_tag'


class TTagBlog(models.Model):
    tag = models.ForeignKey(TTag, models.DO_NOTHING, blank=True, null=True)
    blog = models.ForeignKey(TBlog, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tag_blog'
