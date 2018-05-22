# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:19:36 2018

python web, it worked. run this file in spyder, then open url in browser: http://127.0.0.1:5000/, this url could be got from the running log.

dependency:there are 3 other html files(base.html,entry.html,results.html) together with this py file.

@author: lianzeng
"""

from flask import Flask,render_template,request,redirect


def search4Letters(phrase:str, letters:str):
    ps = set(phrase)
    ls = set(letters)
    return ps.intersection(ls)


app = Flask(__name__)

@app.route('/')
def hello()->'302':
    return redirect('/entry')

@app.route('/search4',methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letter = request.form['letters']
    results =  str(search4Letters(phrase,letter))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letter,
                           the_results=results,
                           the_title = 'Here are results:')

@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html',the_title='Web using Python Flask!')

if __name__ == '__main__':
    app.run()
