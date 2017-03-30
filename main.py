# coding:utf-8
u"""
    main 処理
    __author__ = 'wertrain'
"""
import logging
from google.appengine.ext import blobstore

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
    upload_url = blobstore.create_upload_url('/submitted')
    return render_template('form.html', upload_url=upload_url)

@app.route('/submitted', methods=['POST'])
def submitted_form():
    u"""
        画像アップロード後画面
    """
    comment = escape(request.form['comment'])
    main_image_file = request.files.get('mainImageHidden')
    sub_image1_file = request.files.get('subImage1Hidden')
    sub_image2_file = request.files.get('subImage2Hidden')
    author_name = request.form['authorName']
    delpass = request.form['inputPassword']
    exhibit = request.form['exhibit']

    main_image_data = main_image_file.read() if main_image_file is not None else None
    sub_image1_data = sub_image1_file.read() if sub_image1_file is not None else None
    sub_image2_data = sub_image2_file.read() if sub_image2_file is not None else None

    postdata = {
        'comment': comment,
        'delete_password': delpass,
        'exhibit_flag': exhibit == 'on',
        'author_name': author_name,
        'main_image': main_image_data,
        'sub_image_1': sub_image1_data,
        'sub_image_2': sub_image2_data
    }
    datastore.create_postdata(postdata)
    return render_template(
        'submitted_form.html',
        name=author_name,
        comment=comment)

@app.errorhandler(500)
def server_error(error):
    u"""
        エラー画面
    """
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
