# coding:utf-8
u"""
    main 処理
    __author__ = 'wertrain'
"""
import logging

from flask import Flask, render_template, request
from xml.sax.saxutils import escape
from my.db import datastore

app = Flask(__name__)

@app.route('/')
def home():
    u"""
        ホーム画面
    """
    return render_template('home.html')

@app.route('/form')
def form():
    u"""
        画像アップロード画面
    """
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    u"""
        画像アップロード後画面
    """
    comment = escape(request.form['comment'])
    main = request.form['mainImageHidden']
    sub1 = request.form['subImage1Hidden']
    sub2 = request.form['subImage2Hidden']
    delpass = request.form['inputPassword']
    exhibit = request.form['exhibit']
    postdata = {
        'comment': comment,
        'delete_password': delpass,
        'exhibit_flag': exhibit,
        'main_image': main,
        'sub_image_1': sub1,
        'sub_image_2': sub2
    }
    datastore.create_postdata(postdata)
    return render_template(
        'submitted_form.html',
        name='hello',
        comment=comment)

@app.errorhandler(500)
def server_error(error):
    u"""
        エラー画面
    """
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    logging.exception(error.msg)
    return 'An internal error occurred.', 500
