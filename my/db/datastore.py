# coding:utf-8
u"""
    Google App Engine Datastore ラッパー
    このモジュールは Google App Engine Datastore をラップして使いやすくしたものです。
    __author__ = 'wertrain'
    __version__ = '0.1'
"""
from datetime import datetime
import calendar
from google.appengine.ext import db

class PostData(db.Model):
    u"""
        投稿データモデル
    """
    name = db.StringProperty()
    comment = db.TextProperty()
    delete_password = db.StringProperty()
    exhibit_flag = db.BooleanProperty()
    main_image = db.BlobProperty()
    sub_image_1 = db.BlobProperty()
    sub_image_2 = db.BlobProperty()

def get_postdata_from_id(id):
    u"""
        投稿データを取得
    """
    return PostData.get_by_id(id)

def create_postdata(postdata, data):
    u"""
        投稿データを更新
    """
    postdata = PostData()
    postdata.name = data['name']
    postdata.comment = data['comment']
    postdata.delete_password = data['delete_password']
    postdata.exhibit_flag = data['exhibit_flag']
    postdata.main_image = data['main_image']
    postdata.sub_image_1 = data['sub_image_1']
    postdata.sub_image_2 = data['sub_image_2']
    postdata.put()
    return postdata

def get_postdata():
    u"""
        投稿データを取得
    """
    return PostData.all()

def get_postdata_query():
    u"""
        投稿データのクエリを取得
    """
    return db.Query(PostData)

def remove_all():
    u"""
        投稿データを全削除
    """
    for data in PostData.all():
        data.delete()
