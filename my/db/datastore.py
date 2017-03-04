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
    pid = db.IntegerProperty()
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
    return db.Query(PostData).filter('pid =', pid).get()

def update_postdata(postdata, data):
    postdata = get_postdata_from_id(data[pid])
    if postdata is None:
        postdata = PostData()
    postdata.pid = data[pid]
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
