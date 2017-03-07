# coding:utf-8
u"""
    main 処理
    __author__ = 'wertrain'
"""

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
from xml.sax.saxutils import escape
from my.db import datastore
# [END imports]

app = Flask(__name__)

# [START home]
@app.route('/')
def home():
    return render_template('home.html')
# [END home]

# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]

# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
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
    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name='hello',
        comment=comment)
    # [END render_template]

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
