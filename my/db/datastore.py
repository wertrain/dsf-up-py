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

def get_postdata_from_id(pid):
    u"""
        投稿データを取得
    """
    return PostData.get_by_id(pid)

def create_postdata(data):
    u"""
        投稿データを作成
    """
    postdata = PostData()
    postdata.name = data['author_name']
    postdata.comment = data['comment']
    postdata.delete_password = data['delete_password']
    postdata.exhibit_flag = data['exhibit_flag']
    postdata.main_image = db.Blob(data['main_image']) if data['main_image'] is not None else None
    postdata.sub_image_1 = db.Blob(data['sub_image_1']) if data['sub_image_1'] is not None else None
    postdata.sub_image_2 = db.Blob(data['sub_image_2']) if data['sub_image_2'] is not None else None
    postdata.put()
    return postdata

def delete_postdata(pid):
    u"""
        投稿データを削除
    """
    postdata = get_postdata_from_id(pid)
    if postdata is not None:
        postdata.delete()
        return True
    return False

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
