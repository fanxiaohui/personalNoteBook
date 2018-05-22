
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:19:36 2018

python web, it worked.

open url in browser:   http://127.0.0.1:5000/

@author: lianzeng
"""

from flask import Flask


def search4Letters(phrase:str, letters:str):
    ps = set(phrase)
    ls = set(letters)
    return ps.intersection(ls)


app = Flask(__name__)

@app.route('/')
def hello()->str:
    return 'Great ! hello from flask'

@app.route('/search4')
def do_search()->str:
    return str(search4Letters('i am learning web','aeiou'))

app.run()
