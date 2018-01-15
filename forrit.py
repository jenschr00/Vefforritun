from bottle import *
import os

@route('/')
def index():
    return '''
            <h3>Þetta er síða 1</h3>
            <h1><a href="sida2">Síða 2</a> <a href="sida3">Síða 3</a>  <a href="sida4">Síða 4</a>  </h1>
            '''

@route('/sida2')
def sida2():
    return '''
<h3>Þetta er síða 2</h3>
<h1><a href="/">Síða 1</a></h1>
'''

@route('/sida3')
def sida3():
    return '''
<h3>Þetta er síða 3</h3>
<h1><a href="/">Síða 1</a></h1>
'''

@route('/sida4')
def sida4():
    return '''
<h3>Þetta er síða 4</h3>
<h1><a href="/">Síða 1</a></h1>
'''
    

run(host='0.0.0.0', port=os.environ.get('PORT'))

#run(host='localhost', port=8080)
    
